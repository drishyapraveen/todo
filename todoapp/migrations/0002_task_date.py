# Generated by Django 4.1.7 on 2023-03-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-09-18'),
            preserve_default=False,
        ),
    ]
