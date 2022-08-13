from django.contrib import admin

from .models import Authors

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'soname', 'bio')
    list_display_links = ('name', 'soname')
    search_fields = ('soname', )

admin.site.register(Authors, AuthorsAdmin)
