# Generated by Django 3.2.6 on 2021-09-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0006_auto_20210822_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
