# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20151123_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id',
        ),
        migrations.AlterField(
            model_name='curso',
            name='salon',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
