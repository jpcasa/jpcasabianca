# Generated by Django 2.1 on 2018-10-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20181003_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='program',
            name='summary',
            field=models.CharField(default='', max_length=255),
        ),
    ]