# Generated by Django 2.0.8 on 2018-08-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flick', '0007_groups_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='icon',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
