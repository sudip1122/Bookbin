# Generated by Django 3.0.8 on 2020-09-10 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200910_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address2',
        ),
    ]
