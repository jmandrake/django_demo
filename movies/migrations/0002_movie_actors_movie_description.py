# Generated by Django 4.2.11 on 2024-03-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
