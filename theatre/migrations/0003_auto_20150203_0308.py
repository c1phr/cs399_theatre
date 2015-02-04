# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0002_auto_20150202_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='showtimes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actor',
            name='bio',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
