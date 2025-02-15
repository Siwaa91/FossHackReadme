# Generated by Django 3.1.2 on 2023-10-17 09:59

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('blog', '0001_squashed_0009_auto_20231017_1521'), ('blog', '0002_auto_20231017_1524'), ('blog', '0003_auto_20231017_1525')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2023, 10, 17, 15, 25, 12, 790245))),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
