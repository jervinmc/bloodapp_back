# Generated by Django 4.0.1 on 2022-10-31 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assestment', '0003_assestment_hospital_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assestment',
            name='is_q14',
        ),
    ]