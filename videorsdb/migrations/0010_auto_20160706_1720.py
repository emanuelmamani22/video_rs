# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0009_canal_codigo_canal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='codigo_canal',
            field=models.CharField(max_length=11, blank=True),
        ),
    ]
