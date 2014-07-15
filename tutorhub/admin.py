from django.contrib import admin
from tutorhub.models import *

admin.site.register(Tutor)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Expertise)
admin.site.register(Availability)
admin.site.register(Email_Authentication)

# Register your models here.
