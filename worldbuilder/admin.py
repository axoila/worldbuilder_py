from django.contrib import admin

from .models import World, Entry, Variable

class EntryInline(admin.StackedInline):
    model = Entry
    extra = 0
class WorldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        # ('Entries in this World',  {'fields': ['entry_count']}),
    ]
    inlines = [EntryInline]
    list_display = ['name', 'entry_count']
    search_fields = ['name']
admin.site.register(World, WorldAdmin)

class VariableInline(admin.TabularInline):
    model = Variable
    extra = 0
class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [VariableInline]
    list_display = ['name','variable_count', 'id']
    search_fields = ['name']
admin.site.register(Entry, EntryAdmin)

# class VariableAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['variable_name']}),
#         (None,               {'fields': ['value']}),
#         (None,               {'fields': ['entry']}),
#     ]
#     #inlines = [VariableInline]
#     list_display = ['variable_name',
#     #'variable_count'
#     ]
#     search_fields = ['variable_name']
# admin.site.register(Variable, VariableAdmin)
