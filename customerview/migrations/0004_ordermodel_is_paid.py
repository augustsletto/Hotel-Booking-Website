# Generated by Django 4.2.10 on 2024-02-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerview', '0003_rename_zip_cope_ordermodel_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
