# Generated by Django 3.2 on 2022-12-10 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20221208_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 11, 12, 18, 647308)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 11, 12, 18, 647308)),
        ),
    ]
