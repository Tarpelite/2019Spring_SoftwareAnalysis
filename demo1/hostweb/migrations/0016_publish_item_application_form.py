# Generated by Django 2.2 on 2019-04-24 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostweb', '0015_auto_20190416_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='publish_item_application_form',
            fields=[
                ('created_time', models.DateTimeField(auto_created=True)),
                ('f_ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.TextField(blank=True)),
                ('intro', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0)),
                ('Type', models.CharField(choices=[('P1', 'Paper'), ('P2', 'Patent'), ('P3', 'Project')], max_length=2)),
                ('passed', models.BooleanField(default=False)),
                ('author_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostweb.Author')),
            ],
        ),
    ]
