# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_technicie_list(apps, schema_editor):
    Wbw_list = apps.get_model("meals", "Wbw_list")
    Wbw_list.objects.create(list_id="e52ec42b-3d9a-4a2e-8c40-93c3a2ec85b0", name="Technicie")


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20161006_1640'),
    ]

    operations = [
        migrations.RunPython(add_technicie_list)
    ]
