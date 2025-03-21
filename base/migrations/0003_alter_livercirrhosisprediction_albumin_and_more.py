# Generated by Django 5.0 on 2024-11-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_livercirrhosisprediction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='albumin',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='hepatomegaly',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='n_days',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='platelets',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='prothrombin',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='status',
            field=models.FloatField(max_length=5),
        ),
    ]
