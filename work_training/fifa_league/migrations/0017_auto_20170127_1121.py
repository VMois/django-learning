# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa_league', '0016_auto_20170127_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.FileField(default='../media/static/fifa_league/player/default-player-photo.svg', upload_to='uploads/players/photos/'),
        ),
    ]
