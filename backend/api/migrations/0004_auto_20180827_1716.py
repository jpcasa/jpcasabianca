# Generated by Django 2.0.7 on 2018-08-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180827_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_chart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SkillChart'),
        ),
    ]
