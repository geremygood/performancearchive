from django.contrib import admin
from archive.models import Performance
from archive.models import Performer

class performanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Information', { 'fields' : ['title', 'add_date']}),
    ]

class performerAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Biography', { 'fields' : ['first_name','last_name']}),
    ]

admin.site.register(Performance, performanceAdmin)
admin.site.register(Performer, performerAdmin)
