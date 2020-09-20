# Generated by Django 3.1.1 on 2020-09-20 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start_end_time',
            name='end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='end_time'),
        ),
        migrations.AlterField(
            model_name='start_end_time',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='start_time'),
        ),
    ]
