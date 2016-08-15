# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videorsdb', '0012_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likeanddislike',
            fields=[
                ('id_likeanddislike', models.AutoField(serialize=False, primary_key=True)),
                ('megusta', models.BooleanField(default=False)),
                ('nomegusta', models.BooleanField(default=False)),
                ('id_u', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('id_v', models.ForeignKey(to='videorsdb.UploadVideo')),
            ],
        ),
    ]
