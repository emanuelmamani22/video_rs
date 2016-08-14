# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videorsdb', '0011_auto_20160706_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(serialize=False, primary_key=True)),
                ('comentario_text', models.TextField()),
                ('id_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('id_v', models.ForeignKey(to='videorsdb.UploadVideo')),
            ],
        ),
    ]
