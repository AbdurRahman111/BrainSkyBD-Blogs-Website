# Generated by Django 3.2 on 2022-12-11 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20221211_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 15, 56, 27, 205924)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 15, 56, 27, 205924)),
        ),
    ]
