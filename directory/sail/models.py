from django.db.models import Model, CharField, IntegerField, DateField
from django.db.models import URLField, EmailField, TextField, ImageField
from django.db.models import ForeignKey
from constants import *


class AlumnusProfile(Model):
    """Table for alumni profiles"""

    # Personal
    roll_number = IntegerField()
    title = CharField(max_length= 5, blank=True, null=True)
    first_name = CharField(max_length=50, null=True)
    middle_name = CharField(max_length=50, blank=True, null=True)
    last_name = CharField(max_length=50, blank=True, null=True)
    gender = CharField(max_length=2, blank=True, null=True, choices=GENDERS)
    date_of_birth = DateField(null=True)
    email = EmailField(max_length=100, null=True)
    mobile = CharField(max_length=20, null=True)

    # Educational
    degree = CharField(max_length=40, null=True, choices=DEGREES)
    commencement_year = IntegerField(null=True, choices=COMMENCMENT_YEARS)
    pass_out_year = IntegerField(null=True, choices=PASS_OUT_YEARS)
    department = CharField(max_length=50, null=True, choices=DEPARTMENTS)
    specialization = CharField(max_length=50, blank=True, null=True)
    name_of_guide = CharField(max_length=50, blank=True, null=True)

    # Communication
    alternate_email_id = EmailField(blank=True, null=True)
    alternate_mobile = CharField(max_length=20, blank=True, null=True)
    linkedin_link = URLField(max_length=200, blank=True, null=True)
    research_gate_link = URLField(max_length=200, blank=True, null=True)
    current_address = TextField(null=True)
    current_address_city = CharField(max_length=50, null=True)
    current_address_country = CharField(max_length=50, null=True)
    current_address_zip = CharField(max_length=50, null=True)
    permanent_address = TextField(blank=True, null=True)
    permanent_address_city = CharField(max_length=50, blank=True, null=True)
    permanent_address_country = CharField(max_length=50, blank=True, null=True)
    permanent_address_zip = CharField(max_length=50, blank=True, null=True)

    # Professional
    current_job_occupation = CharField(max_length=50, null=True,
                                       choices=OCCUPATIONS)
    current_job_position = CharField(max_length=50, null=True)
    current_job_company = CharField(max_length=50, null=True)
    current_job_city = CharField(max_length=50, null=True)
    current_job_start_date = DateField(blank=True, null=True)
    current_job_description = CharField(max_length=50, blank=True, null=True)

    # College
    hostel = CharField(max_length=50, blank=True, null=True, choices=HOSTELS)
    room_number = CharField(max_length=50, blank=True, null=True)
    campus_involvements = TextField(blank=True, null=True)

    professional_affiliations = TextField(blank=True, null=True)
    other_interests = TextField(blank=True, null=True)
    about_you = TextField(blank=True, null=True)
    your_message = TextField(blank=True, null=True)
    profile_picture = ImageField(blank=True, null=True, upload_to='Images')

    def __unicode__(self):
        return str(self.roll_number)


class ClubAffiliation(Model):
    """Activity of an alumnus in institute clubs"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    club_affiliation = CharField(max_length=30, blank=True, null=True,
                                 choices=CLUBS)
    club_role = CharField(max_length=80, blank=True, null=True)

class OtherDegree(Model):
    """Degree of an alumnus other than the primary"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    degree = CharField(max_length=40, null=True, choices=DEGREES)
    commencement_year = IntegerField(null=True, choices=COMMENCMENT_YEARS)
    pass_out_year = IntegerField(null=True, choices=PASS_OUT_YEARS)
    department = CharField(max_length=50, null=True, choices=DEPARTMENTS)
    specialization = CharField(max_length=50, blank=True, null=True)

class PastJob(Model):
    """Past job of an alumnus"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    occupation = CharField(max_length=50, null=True,
                                       choices=OCCUPATIONS)
    position = CharField(max_length=50, null=True)
    company = CharField(max_length=50, null=True)
    city = CharField(max_length=50, null=True)
    start_date = DateField(blank=True, null=True)
    description = CharField(max_length=50, blank=True, null=True)
