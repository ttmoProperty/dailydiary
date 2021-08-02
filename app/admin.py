from django.contrib import admin
from .models import Training, Personal_Work, Waaneiza_Work
 
admin.site.site_header = 'Daily Diary of Zwe Linn Htet'
admin.site.index_title = 'Administration Page'
admin.site.site_title = 'Administration Page'


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'website', 'date']
    list_filter = ['instructor', 'website', 'date']
    search_fields = ['title']

class Personal_WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class Waaneiza_WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(Training, TrainingAdmin)
admin.site.register(Personal_Work, Personal_WorkAdmin)
admin.site.register(Waaneiza_Work, Waaneiza_WorkAdmin)
