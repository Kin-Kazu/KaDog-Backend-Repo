# Generated by Django 5.0.1 on 2024-02-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
