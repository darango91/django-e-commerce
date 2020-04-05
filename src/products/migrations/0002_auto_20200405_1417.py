# Generated by Django 2.2.12 on 2020-04-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='coded',
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]