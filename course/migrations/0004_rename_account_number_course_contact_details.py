# Generated by Django 5.0.6 on 2024-06-16 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_course_prerequisites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='account_number',
            new_name='contact_details',
        ),
    ]
