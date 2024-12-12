# Generated by Django 4.2.17 on 2024-12-12 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0004_rental_customer_alter_rental_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
