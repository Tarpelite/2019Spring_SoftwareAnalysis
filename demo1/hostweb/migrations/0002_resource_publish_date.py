# Generated by Django 2.2 on 2019-04-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='publish_date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
