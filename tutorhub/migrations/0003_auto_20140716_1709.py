# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorhub', '0002_auto_20140715_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='instrutor',
            new_name='instructor',
        ),
    ]
