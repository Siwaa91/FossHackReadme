# Generated by Django 3.1.2 on 2023-10-17 07:57

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('news', '0001_initial'), ('news', '0002_auto_20201110_1333'), ('news', '0003_auto_20210111_1244')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('news_title', models.TextField()),
                ('news_description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your news here!')),
                ('news_url', models.URLField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
