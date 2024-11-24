# Generated by Django 5.1.3 on 2024-11-24 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apiwhs', '0003_binmodel_type_binmodel_verification_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binmodel',
            name='id_bin',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(regex='^[0-9A-Z-]*$')]),
        ),
    ]