# Generated by Django 5.0.1 on 2024-02-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_dog_dog_gender'),
        ('events', '0002_remove_event_participants_event_venues_and_more'),
        ('venue', '0002_alter_venueeventsparticipants_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='events',
            field=models.ManyToManyField(through='venue.DogEvent', to='events.event'),
        ),
    ]
