# Generated by Django 3.1.4 on 2020-12-22 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('father_name', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('h_qualification', models.TextField()),
                ('trade', models.CharField(max_length=25)),
                ('work_experience', models.TextField()),
                ('projects', models.TextField()),
                ('achivement', models.TextField()),
                ('certification', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('intrests', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announce_date', models.DateTimeField()),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('img', models.ImageField(upload_to='Announcements/img')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.department')),
            ],
            options={
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]