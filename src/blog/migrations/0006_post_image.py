# Generated by Django 3.1.7 on 2021-05-31 11:16

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210420_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]
