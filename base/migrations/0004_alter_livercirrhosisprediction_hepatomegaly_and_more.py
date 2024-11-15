# Generated by Django 5.0 on 2024-11-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_livercirrhosisprediction_albumin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='hepatomegaly',
            field=models.FloatField(max_length=4),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='n_days',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='platelets',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='status',
            field=models.FloatField(max_length=4),
        ),
    ]