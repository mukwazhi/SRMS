# Generated by Django 2.0.2 on 2018-10-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0009_auto_20181003_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Felix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
            ],
        ),
    ]
