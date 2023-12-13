# Generated by Django 5.0 on 2023-12-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stereo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stereo',
            name='offlineDownload',
            field=models.CharField(blank=True, choices=[('any', 'Any'), ('wifi', 'WI-FI Only Download'), ('mobile', 'Mobile Data')], default='any', max_length=30, null=True),
        ),
    ]