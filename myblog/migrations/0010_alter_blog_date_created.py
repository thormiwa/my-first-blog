# Generated by Django 3.2 on 2021-05-17 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_alter_blog_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 13, 7, 46, 677683, tzinfo=utc)),
        ),
    ]