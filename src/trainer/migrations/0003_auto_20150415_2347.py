# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_auto_20150415_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
