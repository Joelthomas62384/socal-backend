# Generated by Django 5.0 on 2024-11-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0016_alter_notification_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroomdeleted',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
