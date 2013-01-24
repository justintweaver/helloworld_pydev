from hello_polls.models import MyPoll
from hello_polls.models import MyChoice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = MyChoice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')

admin.site.register(MyPoll, PollAdmin)