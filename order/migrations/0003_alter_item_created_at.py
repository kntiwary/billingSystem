# Generated by Django 3.2.6 on 2021-08-15 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_item_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 8, 15, 15, 36, 35, 561100)),
        ),
    ]
