# Generated by Django 4.1 on 2022-08-23 10:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('62fd0eae-a4b6-414d-a2ab-56be6443bfd8'), editable=False, primary_key=True, serialize=False),
        ),
    ]