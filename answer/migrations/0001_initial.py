# Generated by Django 4.0.4 on 2022-06-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('attached_file', models.FileField(null=True, upload_to='QnA/answers/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_edited', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answer.answer')),
            ],
        ),
    ]
