# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
