# Generated by Django 2.2 on 2019-04-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0009_u2e_apply_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
