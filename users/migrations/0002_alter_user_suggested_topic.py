# Generated by Django 4.0.4 on 2022-06-04 08:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='suggested_topic',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), size=None),
        ),
    ]