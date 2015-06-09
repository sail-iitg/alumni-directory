# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sail', '0002_import_data'),
    ]

    operations = [
        migrations.RenameModel('Data', 'AlumnusProfile'),
        migrations.RenameField('AlumnusProfile', 'id', 'roll_number'),
        migrations.RenameField('AlumnusProfile', 'year', 'batch'),
        migrations.RenameField('AlumnusProfile', 'dob', 'date_of_birth'),
        migrations.RenameField('AlumnusProfile', 'ph_no', 'mobile'),
        migrations.RenameField('AlumnusProfile', 'dept', 'department'),
        migrations.RenameField('AlumnusProfile', 'alt_email', 'alternate_email'),
        migrations.RenameField('AlumnusProfile', 'rg_link', 'research_gate_link'),
        migrations.RenameField('AlumnusProfile', 'cur_adrs', 'current_address'),
        migrations.RenameField('AlumnusProfile', 'alt_mob', 'alternate_mobile'),
        migrations.RenameField('AlumnusProfile', 'l_link', 'linkedin_link'),
        migrations.RenameField('AlumnusProfile', 'per_adrs', 'permanent_address'),
        migrations.RenameField('AlumnusProfile', 'per_city', 'permanent_city'),
        migrations.RenameField('AlumnusProfile', 'per_country', 'permanent_country'),
        migrations.RenameField('AlumnusProfile', 'per_pin', 'permanent_pin'),
        migrations.RenameField('AlumnusProfile', 'cur_position', 'current_position'),
        migrations.RenameField('AlumnusProfile', 'startup', 'startup_link')
    ]
