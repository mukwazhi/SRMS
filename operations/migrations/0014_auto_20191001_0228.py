# Generated by Django 2.0.2 on 2019-10-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0013_auto_20190929_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskdetail',
            name='date_of_incident',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='hazard_category',
            field=models.CharField(blank=True, choices=[('Aircraft hazard', 'Aircraft hazard'), ('Personal Injury', 'Personal Injury'), ('Equipment hazard', 'Equipment hazard'), ('Environmental hazard', 'Environmental hazard'), ('personal & equipment hazard', 'Personal & equipment hazard')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='hazard_type',
            field=models.CharField(blank=True, choices=[('Aircraft Related', 'Aircraft Related'), ('Non Aircraft', 'Non Aircraft')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='incident_detail',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='likelyhood',
            field=models.IntegerField(blank=True, choices=[(1, 'Extremely Improbable'), (2, 'Improbable'), (3, 'Remote'), (4, 'Occasional'), (5, 'Frequent')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='location_of_incident',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='proposed_mitigation',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='severity',
            field=models.IntegerField(blank=True, choices=[(1, 'No effect'), (2, 'Slight'), (3, 'Moderate'), (4, 'Major'), (5, 'Serious')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='station',
            field=models.CharField(choices=[('Harare', 'Harare'), ('Victoria Falls', 'Victoria Falls'), ('Bulawayo', 'Bulawayo'), ('Kariba', 'Kariba'), ('Other', 'Other')], default='Harare', max_length=20),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='time_of_incident',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
