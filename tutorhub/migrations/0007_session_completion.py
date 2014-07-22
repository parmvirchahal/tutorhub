# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorhub', '0006_reflection'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='completion',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
