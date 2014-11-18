'''
django admin pages for courseware model
'''
from config_models.admin import ConfigurationModelAdmin

from student.models import UserProfile, UserTestGroup, CourseEnrollmentAllowed, DashboardConfiguration
from student.models import CourseEnrollment, Registration, PendingNameChange, CourseAccessRole, CourseAccessRoleAdmin
from ratelimitbackend import admin
from edraak_validation import UnicodeUserAdmin
from django.contrib.auth.models import User

admin.site.register(UserProfile)

admin.site.register(UserTestGroup)

admin.site.register(CourseEnrollment)

admin.site.register(CourseEnrollmentAllowed)

admin.site.register(Registration)

admin.site.register(PendingNameChange)

admin.site.register(CourseAccessRole, CourseAccessRoleAdmin)

admin.site.register(DashboardConfiguration, ConfigurationModelAdmin)

# Edraak: Support Unicode in admin/user pages
admin.site.register(User, UnicodeUserAdmin)
