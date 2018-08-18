# Generated by Django 2.0.8 on 2018-08-18 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flick', '0015_auto_20180818_1751'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='photos',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='views_count',
        ),
        migrations.AddField(
            model_name='photodetails',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='flick.Photos'),
        ),
    ]
