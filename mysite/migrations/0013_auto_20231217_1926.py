# Generated by Django 2.1.12 on 2023-12-17 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_discussion_contest_self_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion_contest',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.discussion_contest', verbose_name='回复的讨论区id'),
        ),
    ]
