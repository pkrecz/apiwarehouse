# Generated by Django 5.1.3 on 2024-11-25 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_apiwhs', '0008_rename_hu_binmodel_handlingunit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='hu',
            new_name='handlingunit',
        ),
    ]