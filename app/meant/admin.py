
from .models import Contact
from django.contrib.admin import ModelAdmin, site


class ContactConfig(ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'email', 'subject', 'status')
    list_display = ('name','email', 'subject', 'status')
    list_filter = ('status',  'subject')
    ordering = ('-created',)

site.site_header = "Meant4 Admin"
site.register(Contact, ContactConfig)