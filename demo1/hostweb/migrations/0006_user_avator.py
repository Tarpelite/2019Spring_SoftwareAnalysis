# Generated by Django 2.2 on 2019-04-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0005_auto_20190430_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avator',
            field=models.ImageField(blank=True, upload_to='user_avator'),
        ),
    ]