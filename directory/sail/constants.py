"""
Choices for fields in models.
"""
CLUBS = (
    ('alcheringa', 'Alcheringa'),
    ('EDC', 'Entrepreneurial Development Cell (EDC)'),
    ('gymkhana', 'Gymkhana'),
    ('techniche', 'Techniche'),
    ('SAIL', 'Student Alumni Interaction Linkage (SAIL)'),

    ('aeromodelling', 'Aeromodeling Club'),
    ('astronomy', 'Astronomy Club'),
    ('coding', 'Coding Club'),
    ('electronics', 'Electronics Club'),
    ('prakriti', 'Prakriti Club'),
    ('science', 'Science and Quiz Club'),
    ('radioG', 'RadioG'),
    ('robotics', 'Robotics Club'),
    ('finance', 'Finance and Economics Club'),
    ('greenAuto', 'Green Automobile Club'),

    ('anchoring', 'Anchoring Club'),
    ('cadence', 'Cadence Club'),
    ('fineArts', 'Fine Arts Club'),
    ('litSoc', 'LitSoc'),
    ('movie', 'Movie Club'),
    ('music', 'Music Club'),
    ('xpressions', 'Xpressions'),
    ('montage', 'Montage'),
    ('publication', 'Publication Subcommittee'),

    ('aquatics', 'Aquatics Club'),
    ('athletics', 'Athletics Club'),
    ('badminton', 'Badminton Club'),
    ('basketball', 'Basketball Club'),
    ('cricket', 'Cricket Club'),
    ('football', 'Football Club'),
    ('hockey', 'Hockey Club'),
    ('squash', 'Squash Club'),
    ('tableTennis', 'Table Tennis Club'),
    ('tennis', 'Tennis Club'),
    ('volleyball', 'Volleyball Club'),
    ('weightlifting', 'Weightlifting Club'),

    ('interaction', 'Interaction Club'),
    ('benevolence', 'Benevolence Cell'),
    ('social', 'Social Service Club'),
    ('advisory', "Students' Advisory Council"),
    ('youth', 'Youth Empowerment Club'),
    ('rights', 'Rights & Responsibility Club'),
    ('counselling', 'Counselling Cell'),
    ('redRibbon', 'Red Ribbon Club'),
    ('hostel', 'Hostel Affairs Board'),
    ('other', 'Other'),
)
GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)
DEGREES = (
    ('btech', 'B.Tech.'),
    ('mtech', 'M.Tech.'),
    ('bdes', 'B.Des.'),
    ('phd', 'Ph.D.'),
    ('other', 'Other')
)

COMMENCMENT_YEARS = [(i+1994,i+1994) for i in range(37)]
PASS_OUT_YEARS = [(i+1996,i+1996) for i in range(37)]

DEPARTMENTS = (
    ('bt', 'Biotechnology [BT]'),
    ('cl', 'Chemical [CL]'),
    ('che', 'Chemistry [CHE]'),
    ('ce', 'Civil [CE]'),
    ('cse', 'Computer Science [CSE]'),
    ('ds', 'Design [DD]'),
    ('eee', 'Electrical [EEE]'),
    ('ece', 'Electronics [ECE]'),
    ('hss', 'Humanities &amp; Social Sciences [HSS]'),
    ('ma', 'Mathematics [MA]'),
    ('me', 'Mechanical [ME]'),
    ('ep', 'Physics [EP]'),
    ('cfe', 'Centre for Energy'),
    ('cfte', 'Centre for the Environment'),
    ('cnt', 'Centre for Nanotechnology'),
)

OCCUPATIONS = (
    ('scholar', 'Scholar'),
    ('job', 'Job'),
    ('startup', 'Startup/NGO'),
    ('other', 'Other'),
)

HOSTELS = (
    ('barak', 'Barak'),
    ('brahmaputra', 'Brahmaputra'),
    ('dhansiri', 'Dhansiri'),
    ('dibang', 'Dibang'),
    ('dihing', 'Dihing'),
    ('kameng', 'Kameng'),
    ('kapili', 'Kapili'),
    ('lohit', 'Lohit'),
    ('manas', 'Manas'),
    ('married', "Married Scholar's Hostel"),
    ('siang', 'Siang'),
    ('subansiri', 'Subansiri'),
    ('umiam', 'Umiam'),
    ('other', 'Other'),
)