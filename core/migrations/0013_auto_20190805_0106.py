# Generated by Django 2.2.2 on 2019-08-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_student_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bill',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]