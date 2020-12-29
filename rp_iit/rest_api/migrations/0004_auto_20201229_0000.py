# Generated by Django 3.1.4 on 2020-12-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_auto_20201228_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culturalactivity',
            name='student',
        ),
        migrations.AddField(
            model_name='culturalactivity',
            name='student',
            field=models.ManyToManyField(to='rest_api.Student'),
        ),
        migrations.RemoveField(
            model_name='socialactivity',
            name='student',
        ),
        migrations.AddField(
            model_name='socialactivity',
            name='student',
            field=models.ManyToManyField(to='rest_api.Student'),
        ),
        migrations.RemoveField(
            model_name='sport',
            name='student',
        ),
        migrations.AddField(
            model_name='sport',
            name='student',
            field=models.ManyToManyField(to='rest_api.Student'),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='student',
        ),
        migrations.AddField(
            model_name='trip',
            name='student',
            field=models.ManyToManyField(to='rest_api.Student'),
        ),
    ]