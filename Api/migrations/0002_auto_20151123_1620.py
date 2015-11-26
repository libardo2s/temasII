# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grado', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('salon', models.CharField(max_length=10)),
                ('colegio', models.ForeignKey(to='Api.Colegio')),
            ],
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='grado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='colegio',
        ),
        migrations.AddField(
            model_name='docente',
            name='salon',
            field=models.ManyToManyField(to='Api.Curso'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='salon',
            field=models.ForeignKey(to='Api.Curso', null=True),
        ),
    ]
