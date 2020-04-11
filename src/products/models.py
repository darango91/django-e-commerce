from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from .utils import unique_slug_generator, upload_image_path


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, pk):
        qs = self.get_queryset().filter(id=pk)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=20, default='')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default='')
    code = models.CharField(max_length=10, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwarts):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
