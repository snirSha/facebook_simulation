# Generated by Django 3.0.4 on 2020-03-28 14:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0013_auto_20200328_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_requsts',
            name='myfriends_requsts',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=8), size=8),
        ),
    ]
