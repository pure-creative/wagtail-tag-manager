# Generated by Django 2.0.3 on 2018-03-24 14:28

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0002_remove_tag_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
