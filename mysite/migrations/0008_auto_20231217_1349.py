# Generated by Django 2.1.12 on 2023-12-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='scoreboard',
            field=models.TextField(verbose_name='排行榜'),
        ),
    ]
