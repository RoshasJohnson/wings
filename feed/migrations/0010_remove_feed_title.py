# Generated by Django 4.0.4 on 2022-06-13 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_remove_feed_is_dislike_remove_feed_is_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='title',
        ),
    ]