# Generated by Django 5.1.1 on 2024-09-26 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_answer_assessment_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
