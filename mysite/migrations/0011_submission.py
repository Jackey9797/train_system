# Generated by Django 2.1.12 on 2023-12-17 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_selection_able'),
    ]

    operations = [
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_id', models.IntegerField(verbose_name='选拔id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.userinfo', verbose_name='报名人id')),
            ],
        ),
    ]
