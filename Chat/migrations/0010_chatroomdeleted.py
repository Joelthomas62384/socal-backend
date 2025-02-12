# Generated by Django 5.0 on 2024-10-24 00:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0009_remove_chatroom_users_alter_chatroom_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoomDeleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disabled', models.BooleanField(default=False)),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Chat.message')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
