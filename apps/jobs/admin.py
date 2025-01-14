from django.contrib import admin

from apps.jobs.models import Job, Application

admin.site.register(Job)
admin.site.register(Application)