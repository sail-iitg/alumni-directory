from django.contrib import admin
from .models import *

admin.site.register(IITGExperience)
admin.site.register(Achievement)
admin.site.register(Education)
admin.site.register(Job)

class AlumnusProfileAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'gender', 'batch', 'date_of_birth', 'name',
                    'mobile', 'program', 'department', 'guide', 'email',
                    'alternate_email', 'research_gate_link', 'current_address',
                    'city', 'country', 'pin', 'alternate_mobile', 'linkedin_link',
                    'permanent_address', 'permanent_city', 'permanent_country',
                    'permanent_pin', 'current_position', 'past_position_1',
                    'past_position_2', 'startup_link', 'hostel', 'room_no',
                    'campus_involvements_1', 'campus_involvements_2', 'staged_at',
                    'position', 'position_1', 'position_2', 'city_2', 'city_1',
                    'city_3', 'company', 'company_1', 'company_2', 'guidance',
                    'time_stamp')

admin.site.register(AlumnusProfile, AlumnusProfileAdmin)