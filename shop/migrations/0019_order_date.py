# Generated by Django 3.0.8 on 2020-09-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200910_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
    ]
