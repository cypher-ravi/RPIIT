# Generated by Django 3.1.4 on 2020-12-13 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20201213_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.department'),
        ),
    ]
