# Generated by Django 4.0.1 on 2022-11-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0.0, verbose_name='user_id')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]