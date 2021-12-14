# Generated by Django 2.0.7 on 2021-12-10 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('text', models.TextField()),
                ('is_archived', models.NullBooleanField()),
                ('is_deleted', models.NullBooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('linked_notes', models.ManyToManyField(blank=True, related_name='_note_linked_notes_+', to='notes.Note')),
            ],
        ),
    ]