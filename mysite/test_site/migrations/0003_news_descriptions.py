# Generated by Django 3.2.6 on 2021-08-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0002_rename_person_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]