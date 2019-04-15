# Generated by Django 2.2 on 2019-04-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('Type', models.IntegerField()),
                ('introduction', models.TextField()),
                ('institute', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
            ],
        ),
    ]
