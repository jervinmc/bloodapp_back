# Generated by Django 4.0.1 on 2022-10-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_remove_donation_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='hospital_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='hospital_id'),
        ),
    ]