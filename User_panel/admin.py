from django.contrib import admin
from User_panel.models import *
# Register your models here.
@admin.register(Contact_Data)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Email', 'Phone', 'Subject', 'Message', 'Created_at')
    list_display_links = ('id', 'Name')
    search_fields = ('Name', 'Email', 'Subject')
    list_filter = ('Created_at',)
    ordering = ('-Created_at',)
    readonly_fields = ('Created_at',)