# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0008_auto_20160705_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='canal',
            name='codigo_canal',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
