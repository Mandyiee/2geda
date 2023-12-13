# Generated by Django 5.0 on 2023-12-08 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stereo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, choices=[('auto', 'Auto'), ('high', 'High'), ('low', 'Low')], default='auto', max_length=30, null=True)),
                ('offlineDownload', models.CharField(blank=True, choices=[('any', 'Any'), ('wifi', 'WI-FI Only Download'), ('mobile', 'Mobile Data')], default='auto', max_length=30, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stereo', to='userprofile.profile')),
            ],
        ),
    ]