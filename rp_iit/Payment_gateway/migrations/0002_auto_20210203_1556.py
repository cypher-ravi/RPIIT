# Generated by Django 3.1 on 2021-02-03 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Payment_gateway', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
