# Generated by Django 2.1.12 on 2023-12-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='able',
            field=models.IntegerField(default=0, verbose_name='是否可用'),
        ),
    ]
