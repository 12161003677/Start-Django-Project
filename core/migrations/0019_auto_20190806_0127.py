# Generated by Django 2.2.2 on 2019-08-06 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_purchase_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='date',
            new_name='date_p',
        ),
    ]