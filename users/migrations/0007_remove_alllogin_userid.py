# Generated by Django 3.0.4 on 2020-05-11 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alllogin_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alllogin',
            name='userid',
        ),
    ]
