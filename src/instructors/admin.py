from django.contrib import admin

from .models import Instructors,Reviews,Courses,Departments


# Register your models here.
admin.site.register(Instructors)
admin.site.register(Reviews)
admin.site.register(Courses)
admin.site.register(Departments)