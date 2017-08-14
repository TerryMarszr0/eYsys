# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ftp_path',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='have_publish',
            field=models.CharField(max_length=4, default='1'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='have_review',
            field=models.CharField(max_length=4, default='1'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='have_test',
            field=models.CharField(max_length=4, default='1'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='remark',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
