# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0004_downloadvideo_id_u'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='subscriptores',
        ),
        migrations.AddField(
            model_name='perfil',
            name='subscriptores',
            field=models.ManyToManyField(related_name='subscriptores_rel_+', to='videorsdb.Perfil'),
        ),
    ]
