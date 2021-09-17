# Generated by Django 3.2.7 on 2021-09-10 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0013_auto_20210910_1932'),
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
                ('all_text', models.TextField(null=True, verbose_name='Описание публикации')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='News.ncolibrarycategory')),
            ],
            options={
                'verbose_name': 'Публикации ICNL',
            },
        ),
    ]
