# Generated by Django 2.1.7 on 2019-02-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_remove_consolidated_data_variance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cost',
            old_name='code',
            new_name='cost_element',
        ),
    ]
