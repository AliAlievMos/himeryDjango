from django.contrib import admin

from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('cont', )
    list_display_links = ('cont', )
    search_fields = ('cont', )

admin.site.register(Contacts, ContactsAdmin)