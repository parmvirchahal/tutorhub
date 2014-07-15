# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorhub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email_authentication',
            options={'verbose_name': 'Email Authentication'},
        ),
    ]
