# Generated by Django 3.2.7 on 2021-09-10 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0015_auto_20210910_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legislationnko',
            name='name',
        ),
        migrations.DeleteModel(
            name='LegisFavourite',
        ),
        migrations.DeleteModel(
            name='LegislationNKO',
        ),
        migrations.DeleteModel(
            name='NCOCategory',
        ),
    ]