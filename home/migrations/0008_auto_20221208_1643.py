# Generated by Django 3.2 on 2022-12-08 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221207_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 8, 16, 43, 53, 396260)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 8, 16, 43, 53, 397256)),
        ),
    ]
