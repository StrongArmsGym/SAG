# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_signup_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='user_type',
            field=models.CharField(default=b'CL', max_length=2, choices=[(b'CL', b'Client'), (b'TR', b'Trainer'), (b'EM', b'Employee')]),
            preserve_default=True,
        ),
    ]
