# Generated by Django 2.2 on 2019-05-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0007_auto_20190430_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avator',
            field=models.ImageField(blank=True, upload_to='static/author_avator'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avator',
            field=models.ImageField(blank=True, upload_to='demo1/static/user_avator'),
        ),
    ]
