# Generated by Django 2.2.2 on 2019-08-04 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190804_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='usertype',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]