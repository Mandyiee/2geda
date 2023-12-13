# Generated by Django 5.0 on 2023-12-08 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livestreaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoQuality', models.CharField(blank=True, choices=[('auto', 'Auto'), ('higher', 'Higher Picture Quality'), ('saver', 'Data Saver')], default='auto', max_length=30, null=True)),
                ('audioQuality', models.CharField(blank=True, choices=[('auto', 'Auto'), ('high', 'High'), ('low', 'Low')], default='auto', max_length=30, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='livestreaming', to='userprofile.profile')),
            ],
        ),
    ]
