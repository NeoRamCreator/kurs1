# Generated by Django 3.2.6 on 2021-08-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0004_rename_descriptions_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]