# Generated by Django 2.2 on 2019-04-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0018_auto_20190428_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]