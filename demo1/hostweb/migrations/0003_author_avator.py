# Generated by Django 2.2 on 2019-04-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0002_resource_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avator',
            field=models.ImageField(blank=True, upload_to='author_avator'),
        ),
    ]