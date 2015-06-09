from django.db import models
from constants import *

class AlumnusProfile(models.Model):
    """Table for alumni profiles"""

    # Personal
    profile_picture = models.ImageField(blank=True, null=True, upload_to='Images')
    roll_number = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDERS, blank=True, null=True)
    date_of_birth = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    alternate_email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=15, null=True)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
    batch = models.IntegerField(choices=PASS_OUT_YEARS, blank=True, null=True)

    # Institute related
    program = models.CharField(max_length=10, choices=PROGRAMS, blank=True, null=True)
    department = models.CharField(max_length=25, choices=DEPARTMENTS, blank=True, null=True)
    guide = models.CharField(max_length=25, blank=True, null=True)
    research_gate_link = models.CharField(max_length=250, blank=True, null=True)

    # Address
    current_address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    pin = models.IntegerField(null=True)

    permanent_address = models.CharField(max_length=200, null=True)
    permanent_city = models.CharField(max_length=25, null=True)
    permanent_country = models.CharField(max_length=25, blank=True, null=True)
    permanent_pin = models.IntegerField(null=True)

    # Communication
    google_link = models.URLField(max_length=200, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, null=True)

    # Professional
    linkedin_link = models.CharField(max_length=250, blank=True, null=True)
    current_position = models.CharField(max_length=150, choices=OCCUPATIONS, null=True)
    past_position_1 = models.CharField(max_length=150, blank=True, null=True)
    past_position_2 = models.CharField(max_length=150, blank=True, null=True)
    startup_link = models.CharField(max_length=400, blank=True, null=True)
    position = models.TextField(null=True)
    position_1 = models.CharField(max_length=30, blank=True, null=True)
    position_2 = models.CharField(max_length=30, blank=True, null=True)
    city_1 = models.CharField(max_length=50, null=True)
    city_2 = models.CharField(max_length=50, blank=True, null=True)
    city_3 = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, null=True)
    company_1 = models.CharField(max_length=100, blank=True, null=True)
    company_2 = models.CharField(max_length=100, blank=True, null=True)
    guidance = models.IntegerField(blank=True, null=True)

    # Campus
    hostel = models.CharField(max_length=15, choices=HOSTELS, blank=True, null=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    campus_involvements_1 = models.CharField(max_length=200, blank=True, null=True)
    campus_involvements_2 = models.CharField(max_length=200, blank=True, null=True)
    staged_at = models.IntegerField(blank=True, null=True)
    other_interests = models.TextField(blank=True, null=True)
    about_you = models.TextField(blank=True, null=True)
    your_message = models.TextField(blank=True, null=True)
    videos_list = models.TextField(blank=True, null=True)

    time_stamp = models.DateTimeField(blank=True, null=True)

    # Empty stuff, but not to be deleted for importing purposes
    past_position_3 = models.CharField(max_length=150, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    details_1 = models.CharField(max_length=150, blank=True, null=True)
    details_2 = models.CharField(max_length=150, blank=True, null=True)
    details_3 = models.CharField(max_length=150, blank=True, null=True)
    imp_link_2 = models.CharField(max_length=150, blank=True, null=True)
    imp_link_3 = models.CharField(max_length=150, blank=True, null=True)
    any_1 = models.CharField(max_length=150, blank=True, null=True)
    any_2 = models.CharField(max_length=150, blank=True, null=True)
    any_3 = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return str(self.roll_number)


class IITGExperience(models.Model):
    """Activity of an alumnus in institute clubs"""
    alumnus_profile = models.ForeignKey(AlumnusProfile)
    club_name = models.CharField(max_length=30, blank=True, null=True, choices=CLUBS)
    start_date = models.DateField()
    end_date = models.DateField()
    experience = models.TextField()

    def __unicode__(self):
        return str(self.club_name)

class Achievement(models.Model):
    """Achievements received in or out the campus"""
    alumnus_profile = models.ForeignKey(AlumnusProfile)
    year = models.IntegerField()
    achievement = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return str(self.achievement)

class Education(models.Model):
    """Degree of an alumnus other than the primary"""
    alumnus_profile = models.ForeignKey(AlumnusProfile)
    degree = models.CharField(max_length=40, choices=PROGRAMS)
    institute = models.CharField(max_length=100)
    start_year = models.IntegerField(null=True)
    pass_out_year = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return str(self.institute)

class Job(models.Model):
    """Past job of an alumnus"""
    alumnus_profile = models.ForeignKey(AlumnusProfile)
    company = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, null=True, choices=OCCUPATIONS)
    city = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return str(self.company)
