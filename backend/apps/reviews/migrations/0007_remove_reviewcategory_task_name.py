# Generated by Django 4.1.7 on 2023-05-23 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_reviewcategory_task_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewcategory',
            name='task_name',
        ),
    ]