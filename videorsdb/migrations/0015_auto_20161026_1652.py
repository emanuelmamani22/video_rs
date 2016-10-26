# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0014_auto_20161026_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadvideo',
            name='video_file',
            field=models.FileField(max_length=200, upload_to=b'miniatura/'),
        ),
    ]
