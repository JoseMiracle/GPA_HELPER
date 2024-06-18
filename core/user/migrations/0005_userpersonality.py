# Generated by Django 4.2 on 2024-06-18 06:52

import core.utils.enums.base
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_managers_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPersonality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('personality_test', models.URLField()),
                ('study_style', models.CharField(max_length=40)),
                ('other_activities', models.JSONField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personality', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.utils.enums.base.BaseModelBaseMixin, models.Model),
        ),
    ]