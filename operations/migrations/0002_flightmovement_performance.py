# Generated by Django 2.0.2 on 2019-04-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightmovement',
            name='performance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
