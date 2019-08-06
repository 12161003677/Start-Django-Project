# Generated by Django 2.2.2 on 2019-08-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190805_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=8),
            preserve_default=False,
        ),
    ]