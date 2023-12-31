# Generated by Django 3.2.20 on 2023-08-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
