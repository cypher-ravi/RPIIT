# Generated by Django 3.1.4 on 2021-01-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0012_auto_20210102_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='placementcompany',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Social_activity/img'),
        ),
        migrations.AddField(
            model_name='trip',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Trip/img'),
        ),
    ]