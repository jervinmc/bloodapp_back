# Generated by Django 4.0.1 on 2022-10-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assestment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assestment',
            name='is_q1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q1'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q10',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q10'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q11',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q11'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q12',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q12'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q13',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q13'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q14',
            field=models.BooleanField(blank=True, max_length=255, null=True, verbose_name='is_q14'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q2'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q3'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q4'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q5'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q6',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q6'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q7',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q7'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q8',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q8'),
        ),
        migrations.AlterField(
            model_name='assestment',
            name='is_q9',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_q9'),
        ),
    ]
