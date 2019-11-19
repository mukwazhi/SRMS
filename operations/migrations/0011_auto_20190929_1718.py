# Generated by Django 2.0.2 on 2019-09-29 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0010_remove_riskdetail_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskdetail',
            name='action_required',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='reopen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='resources_required',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='riskdetail',
            name='responsible_official',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsible_official', to='operations.Officials'),
        ),
    ]
