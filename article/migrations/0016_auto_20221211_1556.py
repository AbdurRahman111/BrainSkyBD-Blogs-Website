# Generated by Django 3.2 on 2022-12-11 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20221211_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article_table',
            old_name='views',
            new_name='last_hour_views',
        ),
        migrations.AddField(
            model_name='article_table',
            name='total_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='article_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 15, 56, 27, 216956)),
        ),
    ]