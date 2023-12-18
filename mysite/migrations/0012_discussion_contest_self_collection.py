# Generated by Django 2.1.12 on 2023-12-17 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='discussion_contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contents', models.TextField(verbose_name='讨论区内容')),
                ('discussionCon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.contest', verbose_name='比赛id')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.userinfo', verbose_name='用户id')),
                ('response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.discussion', verbose_name='回复的讨论区id')),
            ],
        ),
        migrations.CreateModel(
            name='self_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='题目名')),
                ('url', models.TextField(verbose_name='题目链接')),
                ('solution', models.TextField(verbose_name='题解链接')),
                ('difficulty', models.FloatField(blank=True, null=True, verbose_name='题目难度')),
                ('tag', models.CharField(blank=True, max_length=100, null=True, verbose_name='题目标签')),
                ('source', models.CharField(blank=True, max_length=100, null=True, verbose_name='来源')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.userinfo')),
            ],
        ),
    ]