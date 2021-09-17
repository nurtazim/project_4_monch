# Generated by Django 3.2.7 on 2021-09-10 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0012_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legislationnko',
            old_name='text',
            new_name='title',
        ),
        migrations.CreateModel(
            name='LegisFavourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.legislationnko')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
