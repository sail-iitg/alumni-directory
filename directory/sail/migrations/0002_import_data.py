# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_data_from_sql():
    from directory import settings
    import os
    if (hasattr(settings, 'PATH_TO_DATABASE_IMPORT') and
            os.path.isfile(settings.PATH_TO_DATABASE_IMPORT)):
        sql_statements = open(settings.PATH_TO_DATABASE_IMPORT, 'r').read()
    else:
        sql_statements = ';'
    return sql_statements

class Migration(migrations.Migration):

    dependencies = [
        ('sail', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(load_data_from_sql()),
    ]
