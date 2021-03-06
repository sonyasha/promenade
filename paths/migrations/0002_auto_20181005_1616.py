# Generated by Django 2.1 on 2018-10-05 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geowalk',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='geowalk',
            name='length',
        ),
        migrations.AddField(
            model_name='geowalk',
            name='checked',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='geowalk',
            name='duration_in_seconds',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(86400)]),
        ),
        migrations.AddField(
            model_name='geowalk',
            name='duration_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='geowalk',
            name='length_in_meters',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(20000)]),
        ),
        migrations.AddField(
            model_name='geowalk',
            name='length_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='singlepoint',
            name='checked',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='geowalk',
            name='neighborhood',
            field=models.ManyToManyField(blank=True, to='paths.Neighborhood'),
        ),
    ]
