# Generated by Django 5.0 on 2024-09-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='like',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
