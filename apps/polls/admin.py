from django.contrib import admin

from apps.polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']


admin.site.register(Poll, PollAdmin)