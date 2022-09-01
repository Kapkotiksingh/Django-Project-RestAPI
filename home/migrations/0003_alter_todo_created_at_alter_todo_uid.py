# Generated by Django 4.1 on 2022-08-23 10:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('cdc25bc5-08d6-4bf9-9d15-6effb9cea240'), editable=False, primary_key=True, serialize=False),
        ),
    ]