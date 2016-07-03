# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0005_auto_20160701_2112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DownloadVideo',
            new_name='UploadVideo',
        ),
    ]
