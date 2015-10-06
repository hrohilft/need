# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
