# Generated by Django 2.1 on 2018-10-09 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20181009_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudy',
            name='html',
        ),
    ]