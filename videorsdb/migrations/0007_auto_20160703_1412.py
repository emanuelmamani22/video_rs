# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0006_auto_20160703_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagvideo',
            fields=[
                ('id_tag', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_tag', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='uploadvideo',
            name='id_tag',
            field=models.ForeignKey(default=2, to='videorsdb.Tagvideo'),
            preserve_default=False,
        ),
    ]
