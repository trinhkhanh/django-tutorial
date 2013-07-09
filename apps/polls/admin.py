from django.contrib import admin

from apps.polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Poll, PollAdmin)