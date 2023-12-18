# Generated by Django 2.1.12 on 2023-12-17 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20231211_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='比赛名称')),
                ('date', models.TextField(verbose_name='日期')),
                ('site', models.TextField(verbose_name='参赛链接')),
                ('statement', models.TextField(verbose_name='题面')),
                ('solution', models.TextField(verbose_name='题解')),
                ('scoreboard', models.FloatField(verbose_name='排行榜')),
            ],
        ),
    ]