# Generated by Django 2.0.6 on 2018-06-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cash',
            field=models.FloatField(blank=True, default=0, verbose_name='Tiền mặt'),
        ),
    ]