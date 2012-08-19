from django.contrib import admin
from archive.models import Performance
from archive.models import Venue
from archive.models import Showtime
from archive.models import Group
from archive.models import Performer


class PerformancePerformersInline(admin.TabularInline):
    model = Performer
    extra = 3

class PerformanceShowsInline(admin.TabularInline):
    model = Showtime
    extra = 1

class performerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Biography', { 'fields' : ['first_name','last_name','performance']}),
    ]

class performanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Information', { 'fields' : ['title', 'add_date']}),
    ]
    inlines = [PerformancePerformersInline, PerformanceShowsInline]


    list_display = ('title', 'add_date')
    list_filter = ('title', 'add_date')
    search_fields = ['title']
    ate_hierarchy = 'add_date'

class venueAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Venue Information', { 'fields' : ['name','address','website']}),
        ('Meta Information', { 'fields' : ['add_date']})
    ]


admin.site.register(Performance, performanceAdmin)
admin.site.register(Performer, performerAdmin)
admin.site.register(Venue, venueAdmin)

