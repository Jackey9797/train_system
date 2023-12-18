# Generated by Django 2.1.12 on 2023-12-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_problem_collected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.FloatField(blank=True, null=True, verbose_name='题目难度'),
        ),
        migrations.AddField(
            model_name='question',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='来源'),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='题目标签'),
        ),
    ]
