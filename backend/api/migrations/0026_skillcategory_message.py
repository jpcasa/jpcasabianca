# Generated by Django 2.1 on 2018-10-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_skill_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillcategory',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
