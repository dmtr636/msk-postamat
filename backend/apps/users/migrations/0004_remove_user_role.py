# Generated by Django 4.1.7 on 2023-05-20 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_status_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]