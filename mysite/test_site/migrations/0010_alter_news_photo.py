# Generated by Django 3.2.7 on 2021-09-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0009_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
