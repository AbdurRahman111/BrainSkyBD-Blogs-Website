# Generated by Django 3.2 on 2022-12-07 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 7, 20, 33, 51, 817920))),
            ],
            options={
                'verbose_name_plural': 'Newsletter Table',
            },
        ),
        migrations.AddField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 7, 20, 33, 51, 816923)),
        ),
    ]