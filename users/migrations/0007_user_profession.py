# Generated by Django 4.0.4 on 2022-06-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_avatar_alter_user_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
