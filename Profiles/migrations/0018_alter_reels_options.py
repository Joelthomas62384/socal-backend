# Generated by Django 5.0 on 2024-11-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0017_reels_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reels',
            options={'ordering': ['-thumbnail', '-created_at']},
        ),
    ]
