# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170814_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='have_publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='have_review',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='have_test',
            field=models.BooleanField(default=False),
        ),
    ]
