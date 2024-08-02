# Generated by Django 5.0.3 on 2024-08-02 14:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0009_rename_dogonly_petnames'),
        ('events', '0002_remove_event_participants_event_venues_and_more'),
        ('vaccination', '0006_alter_vaccineuserparticipant_dog'),
        ('venue', '0002_alter_venueeventsparticipants_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PetNames',
            new_name='PetName',
        ),
    ]
