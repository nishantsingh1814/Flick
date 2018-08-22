# Generated by Django 2.0.8 on 2018-08-20 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import flick.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=17, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=255)),
                ('click', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'analytics',
            },
        ),
        migrations.CreateModel(
            name='GroupPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'group_photos',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('flickr_id', models.CharField(max_length=30)),
                ('name', models.CharField(default=None, max_length=255)),
                ('member_count', models.IntegerField(default=0)),
                ('image_count', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('icon', models.ImageField(null=True, upload_to=flick.models.get_image_path)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='PhotoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('comments_count', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'photo_details',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('flickr_id', models.CharField(max_length=30)),
                ('owner', models.CharField(default=None, max_length=255, null=True)),
                ('title', models.CharField(default=None, max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to=flick.models.get_image_path)),
                ('secret', models.CharField(default=None, max_length=30, null=True)),
                ('farm', models.CharField(default=None, max_length=30, null=True)),
                ('server', models.CharField(default=None, max_length=30, null=True)),
                ('date', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.CreateModel(
            name='PhotoTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('tag', models.TextField(blank=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='flick.Photos')),
            ],
            options={
                'db_table': 'photo_tags',
            },
        ),
        migrations.AddField(
            model_name='photodetails',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='flick.Photos'),
        ),
        migrations.AddField(
            model_name='groupphotos',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flick.Groups'),
        ),
        migrations.AddField(
            model_name='groupphotos',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flick.Photos'),
        ),
    ]
