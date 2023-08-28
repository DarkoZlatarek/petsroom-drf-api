# Generated by Django 3.2.20 on 2023-08-28 09:25

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20230821_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, validators=[events.models.Event.validate_date]),
        ),
    ]