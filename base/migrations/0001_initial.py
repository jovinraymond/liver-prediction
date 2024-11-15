# Generated by Django 4.2.16 on 2024-11-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiverCirrhosisPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_days', models.FloatField()),
                ('hepatomegaly', models.FloatField()),
                ('albumin', models.FloatField()),
                ('platelets', models.FloatField()),
                ('prothrombin', models.FloatField()),
                ('status', models.FloatField()),
                ('prediction', models.IntegerField()),
            ],
        ),
    ]
