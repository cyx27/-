# Generated by Django 3.2.5 on 2021-11-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0003_auto_20211127_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='Accusation',
            field=models.CharField(default='', max_length=100),
        ),
    ]
