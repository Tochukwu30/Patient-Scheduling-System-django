# Generated by Django 4.0.6 on 2022-08-04 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_and_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('phone_no', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('speciality', models.CharField(max_length=100, null=True)),
                ('home_addr', models.CharField(max_length=200, null=True)),
                ('office_addr', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('phone_no', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('home_addr', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
