# Generated by Django 2.0.13 on 2019-09-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
