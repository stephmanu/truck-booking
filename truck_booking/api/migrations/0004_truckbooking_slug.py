# Generated by Django 5.0.7 on 2024-08-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_truckcalendar_truckevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckbooking',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
