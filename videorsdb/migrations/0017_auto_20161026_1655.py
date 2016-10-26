# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0016_auto_20161026_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadvideo',
            name='miniatura_video',
            field=models.FileField(max_length=200, upload_to=b'miniatura/', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadvideo',
            name='video_file',
            field=models.FileField(max_length=200, upload_to=b'video/'),
        ),
    ]
