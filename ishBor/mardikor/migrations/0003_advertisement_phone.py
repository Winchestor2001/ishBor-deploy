# Generated by Django 4.0.1 on 2022-02-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mardikor', '0002_category_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
