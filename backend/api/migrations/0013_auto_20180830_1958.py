# Generated by Django 2.0.7 on 2018-08-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180827_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenuitem',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='submenuitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
