# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videorsdb', '0007_auto_20160703_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id_canal', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
                ('id_u', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcriptores',
            fields=[
                ('id_subs', models.AutoField(serialize=False, primary_key=True)),
                ('id_c', models.ForeignKey(to='videorsdb.Canal')),
                ('id_u', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='subscriptores',
        ),
        migrations.RemoveField(
            model_name='uploadvideo',
            name='id_u',
        ),
        migrations.AddField(
            model_name='uploadvideo',
            name='id_c',
            field=models.ForeignKey(default=1, to='videorsdb.Canal'),
            preserve_default=False,
        ),
    ]
