# Generated by Django 5.1.4 on 2025-01-29 00:04

# This migration adds a row to the polls_question table to demonstrate that
# serialized_rollback restores data added by migrations after each test.

from django.db import migrations
from django.utils import timezone

def add_initial_data(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Question.objects.create(question_text="What is your favorite holiday?", pub_date=timezone.now())

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_initial_data
        )
    ]
