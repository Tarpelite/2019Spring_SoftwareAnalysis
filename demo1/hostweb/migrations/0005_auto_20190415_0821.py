# Generated by Django 2.2 on 2019-04-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0004_auto_20190415_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='domain',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='institute',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
