# Generated by Django 4.0 on 2021-12-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
