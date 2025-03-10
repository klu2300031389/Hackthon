# Generated by Django 5.1.1 on 2024-09-27 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def clean_invalid_foreign_keys(apps, schema_editor):
    Assessment = apps.get_model('adminapp', 'Assessment')  # Replace 'adminapp' with your actual app name
    User = apps.get_model(settings.AUTH_USER_MODEL)

    # Get valid user IDs
    valid_user_ids = set(User.objects.values_list('id', flat=True))

    # Clean up invalid references
    for assessment in Assessment.objects.all():
        if assessment.created_by_id and assessment.created_by_id not in valid_user_ids:
            assessment.created_by = None  # Or assign a valid user if necessary
            assessment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_rename_user_employeeresult_employee_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(clean_invalid_foreign_keys),  # Clean existing invalid foreign keys
        migrations.AlterField(
            model_name='assessment',
            name='created_by',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
