# Generated by Django 3.2.7 on 2021-09-04 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image1',
            new_name='image',
        ),
    ]
