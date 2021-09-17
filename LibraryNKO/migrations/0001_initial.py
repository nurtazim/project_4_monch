# Generated by Django 3.2.7 on 2021-09-11 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NCOLibraryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название категории библиотеки')),
            ],
            options={
                'verbose_name': 'Библиотека НКО ',
            },
        ),
        migrations.CreateModel(
            name='PublicationsNKO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок публикации ')),
                ('all_text', models.TextField(null=True, verbose_name='Описание публикации')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryNKO.ncolibrarycategory')),
            ],
            options={
                'verbose_name': 'Публикации ICNL',
            },
        ),
        migrations.CreateModel(
            name='PublicationsFavourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryNKO.publicationsnko')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранное публикации  ',
            },
        ),
    ]
