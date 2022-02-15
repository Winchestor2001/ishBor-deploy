# Generated by Django 4.0.1 on 2022-02-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mardikor', '0003_advertisement_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='condition',
            field=models.CharField(choices=[('Aktiv', 'Aktiv'), ('Yakunlandi', 'Yakunlandi')], default='Aktiv', max_length=50),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='permission',
            field=models.CharField(choices=[('Ha', 'Ha'), ('Yoq', 'Yoq')], default='Yoq', max_length=50),
        ),
    ]