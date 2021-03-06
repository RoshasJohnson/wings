# Generated by Django 4.0.4 on 2022-06-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.TextField(null=True)),
                ('question', models.TextField(null=True)),
                ('attached_file', models.FileField(null=True, upload_to='QnA/answers/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('right_answer', models.IntegerField(default=0, null=True)),
                ('question_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.topic')),
            ],
        ),
    ]
