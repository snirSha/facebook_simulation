# Generated by Django 3.0.4 on 2020-03-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('I like Pizza', 'I like Pizza'), ('Hello World', 'Hello World'), ('What is coronavirus', 'What is coronavirus'), ('What is the meaning of life', 'What is the meaning of life')], default='I like Pizza', max_length=50),
        ),
    ]