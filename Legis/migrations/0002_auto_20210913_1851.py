# Generated by Django 3.2.7 on 2021-09-13 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Legis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Действующее законодательство'), (2, 'Проекты'), (2, 'Действующие документы')], default=1, null=True)),
                ('title', models.CharField(max_length=100)),
                ('all_text', models.TextField(null=True, verbose_name='Описание закона')),
            ],
            options={
                'verbose_name': 'Законы',
            },
        ),
        migrations.RemoveField(
            model_name='legislationnko',
            name='name',
        ),
        migrations.DeleteModel(
            name='NCOCategory',
        ),
        migrations.AlterField(
            model_name='legisfavourite',
            name='legis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legis.law'),
        ),
        migrations.DeleteModel(
            name='LegislationNKO',
        ),
    ]
