# Generated by Django 3.2.4 on 2021-06-03 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210603_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='group_id',
            new_name='group',
        ),
    ]
