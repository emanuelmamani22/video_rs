# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videorsdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id_canal', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_canal', models.CharField(max_length=20)),
                ('duenio_de_canal', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.FileField(max_length=200, upload_to=b'avatar/')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_canal', models.ForeignKey(to='videorsdb.Canal')),
                ('subscriptor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='downloadvideo',
            name='id_u',
        ),
        migrations.AddField(
            model_name='downloadvideo',
            name='id_c',
            field=models.ForeignKey(to='videorsdb.Canal', null=True),
        ),
    ]
