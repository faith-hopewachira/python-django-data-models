# Generated by Django 5.0.6 on 2024-06-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_remove_class_meeting_time_alter_class_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='academic_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='general_performance',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='class',
            name='meeting_days',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.CharField(max_length=20),
        ),
    ]
