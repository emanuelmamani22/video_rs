# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadVideo',
            fields=[
                ('id_video', models.AutoField(serialize=False, primary_key=True)),
                ('cod_video', models.CharField(max_length=11)),
                ('nombre_video', models.CharField(max_length=100)),
                ('video_file', models.FileField(max_length=200, upload_to=b'video/')),
                ('id_u', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
