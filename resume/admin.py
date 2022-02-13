from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'img', 'date_start', 'date_end', 'site')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Job, JobAdmin)
