# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0010_auto_20160706_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='codigo_canal',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
