# Generated by Django 2.1 on 2018-08-30 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180830_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
