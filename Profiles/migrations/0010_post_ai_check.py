# Generated by Django 5.0 on 2024-10-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0009_comment_reply_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ai_check',
            field=models.BooleanField(default=False),
        ),
    ]
