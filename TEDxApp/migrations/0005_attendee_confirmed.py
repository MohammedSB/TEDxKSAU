# Generated by Django 4.0.3 on 2023-02-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEDxApp', '0004_rename_seat_seat_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]