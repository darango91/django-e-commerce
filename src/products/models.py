import random
import os
from django.db import models


def get_file_name_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 39526251522)
    name, ext = get_file_name_ext(filename)
    final_filename = '{}{}'.format(new_filename, ext)
    return 'products/{}/{}'.format(new_filename, final_filename)


class Product(models.Model):
    title = models.CharField(max_length=20, default='')
    description = models.TextField(default='')
    code = models.CharField(max_length=10, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

