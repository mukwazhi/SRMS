# Generated by Django 2.0.2 on 2019-01-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0010_felix'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Felix',
        ),
        migrations.AlterField(
            model_name='trainingrecord',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
