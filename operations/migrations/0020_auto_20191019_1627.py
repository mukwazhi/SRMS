# Generated by Django 2.0.2 on 2019-10-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0019_auto_20191019_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riskdetail',
            old_name='reopen',
            new_name='active_status',
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='residual_severity',
            field=models.IntegerField(blank=True, choices=[(1, 'No effect'), (2, 'Slight'), (3, 'Moderate'), (4, 'Major'), (5, 'Serious')], default=1, null=True),
        ),
    ]
