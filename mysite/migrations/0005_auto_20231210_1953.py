# Generated by Django 2.1.12 on 2023-12-10 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20231210_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='statement',
        ),
    ]
