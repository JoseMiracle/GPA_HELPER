# Generated by Django 4.2 on 2024-06-19 20:57

import core.utils.enums.base
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_academicgoal'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('semester', models.CharField(choices=[('FIRST SEMESTER', 'FIRST_SEMESTER'), ('SECOND SEMESTER', 'SECOND_SEMESTER')], default='FIRST SEMESTER', max_length=15, verbose_name='Course Semester')),
                ('duration', models.CharField(choices=[('ONE MONTH', 'ONE_MONTH'), ('TWO MONTHS', 'TWO_MONTHS'), ('THREE MONTHS', 'THREE_MONTHS'), ('FOUR MONTHS', 'FOUR_MONTHS'), ('FIVE MONTHS', 'FIVE_MONTHS'), ('SIX MONTHS', 'SIX_MONTHS')], default='THREE MONTHS', max_length=12, verbose_name='Semester Duration')),
                ('course_title', models.CharField(max_length=255, verbose_name='Course Title')),
                ('course_code', models.CharField(max_length=255, verbose_name='Course Code')),
                ('unit_load', models.CharField(max_length=255, verbose_name='Unit Load')),
                ('knowledge', models.CharField(choices=[('EASY', 'EASY'), ('MODERATE', 'MODERATE'), ('HARD', 'HARD')], default='MODERATE', max_length=10, verbose_name='Course Knowledge Level')),
                ('uploaded_course', models.FileField(blank=True, null=True, upload_to='gpahelper/uploaded_course/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to=settings.AUTH_USER_MODEL, verbose_name='Course Owner')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
            bases=(core.utils.enums.base.BaseModelBaseMixin, models.Model),
        ),
    ]
