# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa_league', '0009_league_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.FileField(default='../static/fifa_league/gfx/team/default-team-logo.svg', upload_to='uploads/teams/logos/'),
        ),
    ]
