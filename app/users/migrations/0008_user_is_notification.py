# Generated by Django 4.0.1 on 2022-12-18 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_is_assessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_notification',
            field=models.BooleanField(default=True, verbose_name='is_notification'),
        ),
    ]
