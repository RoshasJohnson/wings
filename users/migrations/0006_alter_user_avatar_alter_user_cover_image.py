# Generated by Django 4.0.4 on 2022-06-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_avatar_alter_user_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(null=True, upload_to='UserProfile/avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_image',
            field=models.FileField(null=True, upload_to='UserProfile/cover/'),
        ),
    ]
