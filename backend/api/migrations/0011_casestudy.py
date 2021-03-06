# Generated by Django 2.0.7 on 2018-08-27 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_testimony'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('html', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_studies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
