# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0004_auto_20151006_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('public', models.BooleanField(default=False)),
                ('need', models.ForeignKey(related_name='transl', to='need.Need')),
            ],
        ),
    ]
