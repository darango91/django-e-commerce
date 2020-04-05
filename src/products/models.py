from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20, default='')
    description = models.TextField(default='')
    code = models.CharField(max_length=10, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

