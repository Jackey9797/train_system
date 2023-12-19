# Generated by Django 2.1.12 on 2023-12-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20231217_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='选拔名称')),
                ('sign_d1', models.TextField(verbose_name='报名开始日期')),
                ('sign_d2', models.TextField(verbose_name='报名结束日期')),
                ('select_d1', models.TextField(verbose_name='选拔开始时间')),
                ('select_d2', models.TextField(verbose_name='选拔结束时间')),
                ('need', models.IntegerField(verbose_name='选拔人数')),
            ],
        ),
    ]