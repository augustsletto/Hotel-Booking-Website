# Generated by Django 4.2.10 on 2024-02-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerview', '0004_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
