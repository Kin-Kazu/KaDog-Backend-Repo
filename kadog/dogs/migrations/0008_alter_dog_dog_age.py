# Generated by Django 5.0.1 on 2024-02-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0007_alter_dog_dog_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dog_age',
            field=models.IntegerField(),
        ),
    ]
