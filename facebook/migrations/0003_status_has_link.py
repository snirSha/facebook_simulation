# Generated by Django 3.0.4 on 2020-04-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_auto_20200413_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='has_link',
            field=models.BooleanField(default=False),
        ),
    ]
