from django.db.models import Model, CharField, IntegerField, DateField
from django.db.models import URLField, EmailField, TextField, ImageField
from django.db.models import ForeignKey
from constants import *

class AlumnusProfile(Model):
    """Table for alumni profiles"""

    # Personal
    profile_picture = ImageField(blank=True, null=True, upload_to='Images')
    roll_number = IntegerField()
    title = CharField(max_length=5, blank=True, null=True)
    first_name = CharField(max_length=50, null=True)
    middle_name = CharField(max_length=50, blank=True, null=True)
    last_name = CharField(max_length=50, blank=True, null=True)
    gender = CharField(max_length=2, blank=True, null=True, choices=GENDERS)
    date_of_birth = DateField(null=True)
    webmail = EmailField(max_length=100, null=True)
    mobile = CharField(max_length=20, null=True)
    batch = IntegerField()

    # Address
    current_address = TextField(null=True)
    current_address_city = CharField(max_length=50, null=True)
    current_address_country = CharField(max_length=50, null=True)
    current_address_zip = CharField(max_length=50, null=True)
    
    permanent_address = TextField(blank=True, null=True)
    permanent_address_city = CharField(max_length=50, blank=True, null=True)
    permanent_address_country = CharField(max_length=50, blank=True, null=True)
    permanent_address_zip = CharField(max_length=50, blank=True, null=True)

    # Professional
    # Will be filled by creating a JOB object
    current_job_occupation = CharField(max_length=50, null=True, choices=OCCUPATIONS)
    current_job_company = CharField(max_length=50, null=True)
    current_job_position = CharField(max_length=50, null=True)
    current_job_description = TextField(blank=True, null=True)
    current_job_start_date = DateField(blank=True, null=True)
    current_job_city = CharField(max_length=50, null=True)

    # Educational
    # Nothing    

    # Communication
    alternate_email_id = EmailField(blank=True, null=True)
    alternate_mobile = CharField(max_length=20, blank=True, null=True)
    linkedin_link = URLField(max_length=200, blank=True, null=True)
    google_link = URLField(max_length=200, blank=True, null=True)
    facebook_link = URLField(max_length=200, blank=True, null=True)
    twitter_link = URLField(max_length=200, blank=True, null=True)
    github_link = URLField(max_length=200, blank=True, null=True)
    research_gate_link = URLField(max_length=200, blank=True, null=True)

    # College
    room_number = CharField(max_length=50, blank=True, null=True)
    hostel = CharField(max_length=50, blank=True, null=True, choices=HOSTELS)
    other_interests = TextField(blank=True, null=True)
    about_you = TextField(blank=True, null=True)
    your_message = TextField(blank=True, null=True)
    videos_list = TextField(blank=True, null=True)
    
    def __unicode__(self):
        return str(self.roll_number)


class IITGExperience(Model):
    """Activity of an alumnus in institute clubs"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    club_name = CharField(max_length=30, blank=True, null=True, choices=CLUBS)
    start_date = DateField()
    end_date = DateField()
    experience = TextField()

class Achievement(Model):
    """Achievements received in or out the campus"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    year = IntegerField()
    achievement = CharField(max_length=128)
    description = TextField()


class Education(Model):
    """Degree of an alumnus other than the primary"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    degree = CharField(max_length=40, choices=DEGREES)
    institute = CharField(max_length=100)
    start_year = IntegerField(null=True, choices=COMMENCMENT_YEARS)
    pass_out_year = IntegerField(null=True, choices=PASS_OUT_YEARS)
    # department = CharField(max_length=50, null=True, choices=DEPARTMENTS)
    specialization = CharField(max_length=50, blank=True, null=True)

class Job(Model):
    """Past job of an alumnus"""
    alumnus_profile = ForeignKey(AlumnusProfile)
    company = CharField(max_length=50, null=True)
    position = CharField(max_length=50, null=True)
    start_date = DateField(blank=True, null=True)
    end_date = DateField(blank=True, null=True)
    description = CharField(max_length=50, blank=True, null=True)
    occupation = CharField(max_length=50, null=True, choices=OCCUPATIONS)
    city = CharField(max_length=50, null=True)
