# Generated by Django 5.0 on 2025-03-25 00:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Nome')),
                ('birth_data', models.DateField(verbose_name='Birth Date')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('number', models.CharField(max_length=10, verbose_name='Number')),
                ('issue_date', models.DateField(verbose_name='Issue date')),
                ('expiration_date', models.DateField(verbose_name='Expiration Date')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aula4.person')),
            ],
        ),
    ]
