# Generated by Django 2.0.7 on 2021-12-10 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='linked_notes',
        ),
    ]