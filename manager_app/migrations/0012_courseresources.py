# Generated by Django 2.0.2 on 2019-04-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0011_auto_20190128_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('course', models.ForeignKey(on_delete=None, to='manager_app.Course')),
                ('trainer', models.ForeignKey(on_delete=None, to='manager_app.Trainer')),
            ],
        ),
    ]
