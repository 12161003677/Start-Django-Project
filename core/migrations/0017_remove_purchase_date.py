# Generated by Django 2.2.2 on 2019-08-06 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='date',
        ),
    ]
