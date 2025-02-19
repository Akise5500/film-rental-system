# Generated by Django 4.2.17 on 2024-12-10 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0003_remove_rental_customer_film_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(),
        ),
    ]
