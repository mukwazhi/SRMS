# Generated by Django 2.0.2 on 2019-10-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0015_auto_20191001_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('archive', models.BooleanField(default=False)),
                ('document_type', models.CharField(choices=[('Manual', 'Manual'), ('Form', 'Form'), ('Checklist', 'Checklist'), ('Bulletin', 'Bulletin')], max_length=50)),
            ],
        ),
    ]
