# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('trainer', 'trainer level permissions'), ('employee', 'employee level permissions'), ('client', 'client level permissions')),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_trainer',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
