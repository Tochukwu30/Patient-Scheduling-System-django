# Generated by Django 4.0.6 on 2022-08-22 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
