# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0003_auto_20151006_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='where',
            field=models.CharField(max_length=1, default='H', choices=[('H', 'HWBR'), ('E', 'Emporhalle'), ('P', 'Physik')]),
        ),
    ]
