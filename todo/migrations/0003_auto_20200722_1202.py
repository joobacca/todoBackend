# Generated by Django 3.0.8 on 2020-07-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='owner',
        ),
    ]
