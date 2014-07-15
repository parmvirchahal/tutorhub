# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tutor_email', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Availabilities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email_Authentication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tutor_email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tutor_email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Expertise',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('instructor_email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('classes', models.CharField(max_length=25, choices=[('English', 'English'), ('Social Studies', 'Social Studies'), ('Science', 'Science'), ('Mathematics', 'Mathematics'), ('Fine Arts', 'Fine Arts (Art, Music, Theatre)'), ('Business', 'Business/Marketing'), ('IB', 'IB/TOK'), ('AVID', 'AVID'), ('PE', "PE/Health/Driver's Education"), ('JROTC', 'JROTC'), ('SAT', 'SAT Prep/ACT Prep/ Test Prep'), ('ESOL', 'ESOL'), ('World Languages', 'World Langauges'), ('Other', 'Independent/Other')])),
                ('building', models.CharField(max_length=25)),
                ('room', models.CharField(max_length=25)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=35)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('building', models.CharField(max_length=25)),
                ('room', models.CharField(max_length=4)),
                ('subject', models.CharField(max_length=25, choices=[('English', 'English'), ('Social Studies', 'Social Studies'), ('Science', 'Science'), ('Mathematics', 'Mathematics'), ('Fine Arts', 'Fine Arts (Art, Music, Theatre)'), ('Business', 'Business/Marketing'), ('IB', 'IB/TOK'), ('AVID', 'AVID'), ('PE', "PE/Health/Driver's Education"), ('JROTC', 'JROTC'), ('SAT', 'SAT Prep/ACT Prep/ Test Prep'), ('ESOL', 'ESOL'), ('World Languages', 'World Langauges'), ('Other', 'Independent/Other')])),
                ('instrutor', models.CharField(max_length=25)),
                ('assignment', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=2, choices=[('9', 'Ninth Grade'), ('10', 'Tenth Grade'), ('11', 'Eleventh Grade'), ('12', 'Twelfth Grade')])),
                ('apt_time', models.CharField(max_length=25, choices=[('B1D1', 'Block 1 Day 1'), ('B1D2', 'Block 1 Day 2'), ('B2D1', 'Block 2 Day 1'), ('B2D2', 'Block 2 Day 2'), ('B3D1', 'Block 3 Day 1'), ('B3D2', 'Block 3 Day 2'), ('B4D1', 'Block 4 Day 1'), ('B4D2', 'Block 4 Day 2'), ('A', 'A Lunch'), ('B', 'B Lunch'), ('C', 'C Lunch'), ('Eagle Time', 'Eagle Time'), ('After School Monday', 'After School Monday'), ('After School Thursday', 'After School Thursday')])),
                ('reason_visited', models.CharField(max_length=50, choices=[('Teacher required', 'It was teacher required.'), ('Teacher offered extra credit', 'My teacher offered extra credit.'), ('Been before and found it useful', 'I have been here before and found it useful.'), ('Heard about it and wanted to try', 'I heard about it and wanted to give it a try.'), ('Rewriting and resubmitting essay', 'I am rewriting and resubmitting an essay.')])),
                ('visited', models.CharField(max_length=50, choices=[('Never', 'I have never been to the EWC before.'), ('Not this school year', 'Yes, but not this school year.'), ('Already been this school year', 'Yes, I have already been here this school year.')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=35)),
                ('student_email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('grade', models.CharField(max_length=2, choices=[('9', 'Ninth Grade'), ('10', 'Tenth Grade'), ('11', 'Eleventh Grade'), ('12', 'Twelfth Grade')])),
                ('email', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=35)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tutor_email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('picture', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
