# Generated by Django 3.2.5 on 2022-01-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0010_datatext_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatext',
            name='Courts',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
