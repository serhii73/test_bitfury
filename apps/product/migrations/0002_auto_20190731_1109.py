# Generated by Django 2.2.3 on 2019-07-31 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productowners',
            old_name='product',
            new_name='object',
        ),
    ]
