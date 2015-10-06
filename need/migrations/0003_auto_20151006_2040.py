# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0002_auto_20151006_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='where',
            field=models.CharField(choices=[('HWBR', 'HWBR'), ('Emporhalle', 'Emporhalle'), ('Physik', 'Physik')], max_length=1, default='HWBR'),
        ),
    ]
