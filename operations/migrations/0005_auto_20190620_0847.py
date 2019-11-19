# Generated by Django 2.0.2 on 2019-06-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_officials_riskdetail_riskevaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskevaluation',
            name='evidence_of_closure',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='likelyhood',
            field=models.IntegerField(choices=[(1, 'Extremely Improbable'), (2, 'Improbable'), (3, 'Remote'), (4, 'Occasional'), (5, 'Frequent')], default=1),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='severity',
            field=models.IntegerField(choices=[(1, 'No effect'), (2, 'Slight'), (3, 'Moderate'), (4, 'Major'), (5, 'Serious')], default=1),
        ),
    ]
