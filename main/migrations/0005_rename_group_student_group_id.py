# Generated by Django 3.2.4 on 2021-06-03 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210603_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='group',
            new_name='group_id',
        ),
    ]
