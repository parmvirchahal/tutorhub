# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorhub', '0004_remove_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apt_Time',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='availability',
            name='blocks',
            field=models.ForeignKey(to='tutorhub.Apt_Time', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='availability',
            name='tutor',
            field=models.ForeignKey(to='tutorhub.Tutor', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='availability',
            name='tutor_email',
        ),
        migrations.AlterField(
            model_name='availability',
            name='date',
            field=models.DateField(null=True, verbose_name='absent'),
        ),
    ]
