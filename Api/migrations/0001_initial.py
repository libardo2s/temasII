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
            name='Colegio',
            fields=[
                ('codigo', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(default=b'Moroso', max_length=12, choices=[(b'Paz y salvo', b'Paz y salvo'), (b'Moroso', b'Moroso')])),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('tipo_documento', models.CharField(max_length=20, choices=[(b'Cedula de ciudadania', b'Cedula de ciudadania'), (b'Tarjeta de identidad', b'Tarjeta de identidad'), (b'Cedula Extranjera', b'Cedula Extranjera'), (b'Registro Civil', b'Registro Civil')])),
                ('documento', models.IntegerField(serialize=False, primary_key=True)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50, null=True)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('sexo', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntuacion', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Api.Persona')),
            ],
            bases=('Api.persona',),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Api.Persona')),
                ('grado', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
            ],
            bases=('Api.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='colegio',
            field=models.ForeignKey(to='Api.Colegio'),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='puntuacion',
            name='estudiante',
            field=models.ForeignKey(to='Api.Estudiante'),
        ),
    ]
