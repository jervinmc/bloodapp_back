# Generated by Django 4.0.1 on 2022-07-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_marital_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='birthdate'),
        ),
        migrations.AddField(
            model_name='user',
            name='blood_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='blood_type'),
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mobile_number'),
        ),
        migrations.AddField(
            model_name='user',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='permanent_address'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='user_type'),
        ),
    ]
