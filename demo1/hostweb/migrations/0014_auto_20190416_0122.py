# Generated by Django 2.2 on 2019-04-16 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0013_auto_20190416_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bind',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='hostweb.User'),
        ),
    ]