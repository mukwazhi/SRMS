# Generated by Django 2.0.2 on 2018-09-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0005_trainingrecord_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingrecord',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='manager_app_media/'),
        ),
    ]
