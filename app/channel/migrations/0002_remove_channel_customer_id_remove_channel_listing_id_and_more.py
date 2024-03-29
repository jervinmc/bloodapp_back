# Generated by Django 4.0.1 on 2022-10-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='seller_id',
        ),
        migrations.AddField(
            model_name='channel',
            name='finder_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='finder_id'),
        ),
        migrations.AddField(
            model_name='channel',
            name='hospital_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='hospital_id'),
        ),
    ]
