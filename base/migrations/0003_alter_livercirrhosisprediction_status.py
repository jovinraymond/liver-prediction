# Generated by Django 4.2.16 on 2025-03-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_livercirrhosisprediction_drug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livercirrhosisprediction',
            name='status',
            field=models.IntegerField(max_length=4),
        ),
    ]
