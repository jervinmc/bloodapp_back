# Generated by Django 4.0.1 on 2022-11-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_latitude_user_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='no_donate',
            field=models.IntegerField(default=0.0, verbose_name='no_donate'),
        ),
    ]
