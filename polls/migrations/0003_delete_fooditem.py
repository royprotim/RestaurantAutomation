# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170328_1836'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]
