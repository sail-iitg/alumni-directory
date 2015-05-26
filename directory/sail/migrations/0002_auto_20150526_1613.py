# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sail', '0001_initial'),
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
                ('degree', models.CharField(max_length=40, choices=[(b'btech', b'B.Tech.'), (b'mtech', b'M.Tech.'), (b'bdes', b'B.Des.'), (b'phd', b'Ph.D.'), (b'other', b'Other')])),
                ('institute', models.CharField(max_length=100)),
                ('start_year', models.IntegerField(null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)])),
                ('pass_out_year', models.IntegerField(null=True, choices=[(1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032)])),
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
        migrations.RemoveField(
            model_name='clubaffiliation',
            name='alumnus_profile',
        ),
        migrations.RemoveField(
            model_name='otherdegree',
            name='alumnus_profile',
        ),
        migrations.RemoveField(
            model_name='pastjob',
            name='alumnus_profile',
        ),
        migrations.RenameField(
            model_name='alumnusprofile',
            old_name='email',
            new_name='webmail',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='campus_involvements',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='commencement_year',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='name_of_guide',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='pass_out_year',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='professional_affiliations',
        ),
        migrations.RemoveField(
            model_name='alumnusprofile',
            name='specialization',
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='batch',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='facebook_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='github_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='google_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='twitter_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumnusprofile',
            name='videos_list',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alumnusprofile',
            name='current_job_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='ClubAffiliation',
        ),
        migrations.DeleteModel(
            name='OtherDegree',
        ),
        migrations.DeleteModel(
            name='PastJob',
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
