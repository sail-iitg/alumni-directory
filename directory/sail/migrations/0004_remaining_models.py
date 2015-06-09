# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sail', '0003_rename_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('achievement', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=40, choices=[(b'b', b'B.Tech.'), (b'm', b'M.Tech.'), (b'bd', b'B.Des.'), (b'p', b'Ph.D.'), (b'other', b'Other')])),
                ('institute', models.CharField(max_length=100)),
                ('start_year', models.IntegerField(null=True)),
                ('pass_out_year', models.IntegerField(null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('specialization', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IITGExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(blank=True, max_length=30, null=True, choices=[(b'alcheringa', b'Alcheringa'), (b'EDC', b'Entrepreneurial Development Cell (EDC)'), (b'gymkhana', b'Gymkhana'), (b'techniche', b'Techniche'), (b'SAIL', b'Student Alumni Interaction Linkage (SAIL)'), (b'aeromodelling', b'Aeromodeling Club'), (b'astronomy', b'Astronomy Club'), (b'coding', b'Coding Club'), (b'electronics', b'Electronics Club'), (b'prakriti', b'Prakriti Club'), (b'science', b'Science and Quiz Club'), (b'radioG', b'RadioG'), (b'robotics', b'Robotics Club'), (b'finance', b'Finance and Economics Club'), (b'greenAuto', b'Green Automobile Club'), (b'anchoring', b'Anchoring Club'), (b'cadence', b'Cadence Club'), (b'fineArts', b'Fine Arts Club'), (b'litSoc', b'LitSoc'), (b'movie', b'Movie Club'), (b'music', b'Music Club'), (b'xpressions', b'Xpressions'), (b'montage', b'Montage'), (b'publication', b'Publication Subcommittee'), (b'aquatics', b'Aquatics Club'), (b'athletics', b'Athletics Club'), (b'badminton', b'Badminton Club'), (b'basketball', b'Basketball Club'), (b'cricket', b'Cricket Club'), (b'football', b'Football Club'), (b'hockey', b'Hockey Club'), (b'squash', b'Squash Club'), (b'tableTennis', b'Table Tennis Club'), (b'tennis', b'Tennis Club'), (b'volleyball', b'Volleyball Club'), (b'weightlifting', b'Weightlifting Club'), (b'interaction', b'Interaction Club'), (b'benevolence', b'Benevolence Cell'), (b'social', b'Social Service Club'), (b'advisory', b"Students' Advisory Council"), (b'youth', b'Youth Empowerment Club'), (b'rights', b'Rights & Responsibility Club'), (b'counselling', b'Counselling Cell'), (b'redRibbon', b'Red Ribbon Club'), (b'hostel', b'Hostel Affairs Board'), (b'other', b'Other')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('experience', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=50, null=True, blank=True)),
                ('occupation', models.CharField(max_length=50, null=True, choices=[(b'scholar', b'Scholar'), (b'job', b'Job'), (b'startup', b'Startup/NGO'), (b'other', b'Other')])),
                ('city', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='alumnus_profile',
            field=models.ForeignKey(to='sail.AlumnusProfile'),
        ),
        migrations.AddField(
            model_name='iitgexperience',
            name='alumnus_profile',
            field=models.ForeignKey(to='sail.AlumnusProfile'),
        ),
        migrations.AddField(
            model_name='education',
            name='alumnus_profile',
            field=models.ForeignKey(to='sail.AlumnusProfile'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='alumnus_profile',
            field=models.ForeignKey(to='sail.AlumnusProfile'),
        ),
    ]
