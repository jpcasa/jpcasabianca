# Generated by Django 2.1 on 2018-10-12 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20181012_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submenuitem',
            options={'ordering': ['order']},
        ),
    ]