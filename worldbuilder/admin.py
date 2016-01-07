from django.contrib import admin

from .models import World, Entry, Variable

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 0

class WorldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['world_name']}),
    ]
    inlines = [EntryInline]
    list_display = ('world_name', 'entry_count')
    search_fields = ['world_name']
admin.site.register(World, WorldAdmin)
