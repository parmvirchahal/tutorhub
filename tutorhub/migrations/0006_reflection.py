# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorhub', '0005_auto_20140722_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('reflection', models.TextField()),
                ('instructor', models.ForeignKey(null=True, to='tutorhub.Instructor')),
                ('session', models.ForeignKey(null=True, to='tutorhub.Session')),
                ('student', models.ForeignKey(null=True, to='tutorhub.Student')),
                ('tutor', models.ForeignKey(null=True, to='tutorhub.Tutor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
