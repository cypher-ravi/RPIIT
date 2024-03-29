# Generated by Django 3.1 on 2021-02-03 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0001_initial'),
        ('Payment_gateway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredtrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegisteredTrip', to='rest_api.trip'),
        ),
        migrations.AddField(
            model_name='registeredtrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='order_summary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Payment_gateway.registeredtrip'),
        ),
    ]
