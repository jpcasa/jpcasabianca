# Generated by Django 2.0.7 on 2018-08-27 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20180827_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('company_logo', models.CharField(max_length=255)),
                ('company_website', models.URLField()),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('responsibilities', models.CharField(max_length=255)),
                ('achievements', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
