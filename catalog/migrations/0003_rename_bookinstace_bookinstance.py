# Generated by Django 4.2.18 on 2025-01-22 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInstace',
            new_name='BookInstance',
        ),
    ]
