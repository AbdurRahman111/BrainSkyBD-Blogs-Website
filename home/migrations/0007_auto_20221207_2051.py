# Generated by Django 3.2 on 2022-12-07 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20221207_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 7, 20, 51, 52, 357821)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 7, 20, 51, 52, 358818)),
        ),
    ]
