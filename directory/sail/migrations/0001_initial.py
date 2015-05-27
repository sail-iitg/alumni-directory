# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnusProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_number', models.IntegerField()),
                ('title', models.CharField(max_length=5, null=True, blank=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=2, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('degree', models.CharField(max_length=40, null=True, choices=[(b'btech', b'B.Tech.'), (b'mtech', b'M.Tech.'), (b'bdes', b'B.Des.'), (b'phd', b'Ph.D.'), (b'other', b'Other')])),
                ('commencement_year', models.IntegerField(null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)])),
                ('pass_out_year', models.IntegerField(null=True, choices=[(1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032)])),
                ('department', models.CharField(max_length=50, null=True, choices=[(b'bt', b'Biotechnology [BT]'), (b'cl', b'Chemical [CL]'), (b'che', b'Chemistry [CHE]'), (b'ce', b'Civil [CE]'), (b'cse', b'Computer Science [CSE]'), (b'ds', b'Design [DD]'), (b'eee', b'Electrical [EEE]'), (b'ece', b'Electronics [ECE]'), (b'hss', b'Humanities &amp; Social Sciences [HSS]'), (b'ma', b'Mathematics [MA]'), (b'me', b'Mechanical [ME]'), (b'ep', b'Physics [EP]'), (b'cfe', b'Centre for Energy'), (b'cfte', b'Centre for the Environment'), (b'cnt', b'Centre for Nanotechnology')])),
                ('specialization', models.CharField(max_length=50, null=True, blank=True)),
                ('name_of_guide', models.CharField(max_length=50, null=True, blank=True)),
                ('alternate_email_id', models.EmailField(max_length=254, null=True, blank=True)),
                ('alternate_mobile', models.CharField(max_length=20, null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('research_gate_link', models.URLField(null=True, blank=True)),
                ('current_address', models.TextField(null=True)),
                ('current_address_city', models.CharField(max_length=50, null=True)),
                ('current_address_country', models.CharField(max_length=50, null=True)),
                ('current_address_zip', models.CharField(max_length=50, null=True)),
                ('permanent_address', models.TextField(null=True, blank=True)),
                ('permanent_address_city', models.CharField(max_length=50, null=True, blank=True)),
                ('permanent_address_country', models.CharField(max_length=50, null=True, blank=True)),
                ('permanent_address_zip', models.CharField(max_length=50, null=True, blank=True)),
                ('current_job_occupation', models.CharField(max_length=50, null=True, choices=[(b'scholar', b'Scholar'), (b'job', b'Job'), (b'startup', b'Startup/NGO'), (b'other', b'Other')])),
                ('current_job_position', models.CharField(max_length=50, null=True)),
                ('current_job_company', models.CharField(max_length=50, null=True)),
                ('current_job_city', models.CharField(max_length=50, null=True)),
                ('current_job_start_date', models.DateField(null=True, blank=True)),
                ('current_job_description', models.CharField(max_length=50, null=True, blank=True)),
                ('hostel', models.CharField(blank=True, max_length=50, null=True, choices=[(b'barak', b'Barak'), (b'brahmaputra', b'Brahmaputra'), (b'dhansiri', b'Dhansiri'), (b'dibang', b'Dibang'), (b'dihing', b'Dihing'), (b'kameng', b'Kameng'), (b'kapili', b'Kapili'), (b'lohit', b'Lohit'), (b'manas', b'Manas'), (b'married', b"Married Scholar's Hostel"), (b'siang', b'Siang'), (b'subansiri', b'Subansiri'), (b'umiam', b'Umiam'), (b'other', b'Other')])),
                ('room_number', models.CharField(max_length=50, null=True, blank=True)),
                ('campus_involvements', models.TextField(null=True, blank=True)),
                ('professional_affiliations', models.TextField(null=True, blank=True)),
                ('other_interests', models.TextField(null=True, blank=True)),
                ('about_you', models.TextField(null=True, blank=True)),
                ('your_message', models.TextField(null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'Images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubAffiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_affiliation', models.CharField(blank=True, max_length=30, null=True, choices=[(b'alcheringa', b'Alcheringa'), (b'EDC', b'Entrepreneurial Development Cell (EDC)'), (b'gymkhana', b'Gymkhana'), (b'techniche', b'Techniche'), (b'SAIL', b'Student Alumni Interaction Linkage (SAIL)'), (b'aeromodelling', b'Aeromodeling Club'), (b'astronomy', b'Astronomy Club'), (b'coding', b'Coding Club'), (b'electronics', b'Electronics Club'), (b'prakriti', b'Prakriti Club'), (b'science', b'Science and Quiz Club'), (b'radioG', b'RadioG'), (b'robotics', b'Robotics Club'), (b'finance', b'Finance and Economics Club'), (b'greenAuto', b'Green Automobile Club'), (b'anchoring', b'Anchoring Club'), (b'cadence', b'Cadence Club'), (b'fineArts', b'Fine Arts Club'), (b'litSoc', b'LitSoc'), (b'movie', b'Movie Club'), (b'music', b'Music Club'), (b'xpressions', b'Xpressions'), (b'montage', b'Montage'), (b'publication', b'Publication Subcommittee'), (b'aquatics', b'Aquatics Club'), (b'athletics', b'Athletics Club'), (b'badminton', b'Badminton Club'), (b'basketball', b'Basketball Club'), (b'cricket', b'Cricket Club'), (b'football', b'Football Club'), (b'hockey', b'Hockey Club'), (b'squash', b'Squash Club'), (b'tableTennis', b'Table Tennis Club'), (b'tennis', b'Tennis Club'), (b'volleyball', b'Volleyball Club'), (b'weightlifting', b'Weightlifting Club'), (b'interaction', b'Interaction Club'), (b'benevolence', b'Benevolence Cell'), (b'social', b'Social Service Club'), (b'advisory', b"Students' Advisory Council"), (b'youth', b'Youth Empowerment Club'), (b'rights', b'Rights & Responsibility Club'), (b'counselling', b'Counselling Cell'), (b'redRibbon', b'Red Ribbon Club'), (b'hostel', b'Hostel Affairs Board'), (b'other', b'Other')])),
                ('club_role', models.CharField(max_length=80, null=True, blank=True)),
                ('alumnus_profile', models.ForeignKey(to='sail.AlumnusProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDegree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=40, null=True, choices=[(b'btech', b'B.Tech.'), (b'mtech', b'M.Tech.'), (b'bdes', b'B.Des.'), (b'phd', b'Ph.D.'), (b'other', b'Other')])),
                ('commencement_year', models.IntegerField(null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)])),
                ('pass_out_year', models.IntegerField(null=True, choices=[(1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032)])),
                ('department', models.CharField(max_length=50, null=True, choices=[(b'bt', b'Biotechnology [BT]'), (b'cl', b'Chemical [CL]'), (b'che', b'Chemistry [CHE]'), (b'ce', b'Civil [CE]'), (b'cse', b'Computer Science [CSE]'), (b'ds', b'Design [DD]'), (b'eee', b'Electrical [EEE]'), (b'ece', b'Electronics [ECE]'), (b'hss', b'Humanities &amp; Social Sciences [HSS]'), (b'ma', b'Mathematics [MA]'), (b'me', b'Mechanical [ME]'), (b'ep', b'Physics [EP]'), (b'cfe', b'Centre for Energy'), (b'cfte', b'Centre for the Environment'), (b'cnt', b'Centre for Nanotechnology')])),
                ('specialization', models.CharField(max_length=50, null=True, blank=True)),
                ('alumnus_profile', models.ForeignKey(to='sail.AlumnusProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PastJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occupation', models.CharField(max_length=50, null=True, choices=[(b'scholar', b'Scholar'), (b'job', b'Job'), (b'startup', b'Startup/NGO'), (b'other', b'Other')])),
                ('position', models.CharField(max_length=50, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=50, null=True, blank=True)),
                ('alumnus_profile', models.ForeignKey(to='sail.AlumnusProfile')),
            ],
        ),
    ]
