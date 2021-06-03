# Generated by Django 3.2.4 on 2021-06-03 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210603_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='attachments',
            field=models.FileField(blank=True, upload_to='../files/lectures/', verbose_name='Матеріали'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Назва задачі')),
                ('description', models.TextField(verbose_name='Умова Задачі')),
                ('testfile', models.FileField(blank=True, upload_to='../files/tasks/', verbose_name='Матеріали')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.group')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачі',
                'db_table': 'tb_tasks',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.FileField(blank=True, upload_to='../files/tasks/', verbose_name='Матеріали')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='main.student')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='main.task')),
            ],
            options={
                'verbose_name': "Розв'язок",
                'verbose_name_plural': "Розв'язки",
                'db_table': 'tb_solutions',
            },
        ),
    ]
