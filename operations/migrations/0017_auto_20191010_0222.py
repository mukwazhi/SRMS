# Generated by Django 2.0.2 on 2019-10-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0016_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskdetail',
            name='original_report',
            field=models.FileField(blank=True, null=True, upload_to='scans/'),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='evidence_of_closure',
            field=models.FileField(blank=True, null=True, upload_to='evidence/'),
        ),
    ]
