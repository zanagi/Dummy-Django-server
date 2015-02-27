# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sensor', models.CharField(unique=True, max_length=250)),
                ('value', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
