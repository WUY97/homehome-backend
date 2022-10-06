# Generated by Django 4.1.1 on 2022-09-30 21:37

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('type', models.CharField(choices=[('University', 'University'), ('Hospital', 'Hospital'), ('Stadium', 'Stadium')], max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='location',
        ),
        migrations.AddField(
            model_name='listing',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
