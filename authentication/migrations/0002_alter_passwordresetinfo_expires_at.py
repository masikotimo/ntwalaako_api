# Generated by Django 3.2.4 on 2023-06-06 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 12, 29, 4, 852449, tzinfo=utc)),
        ),
    ]
