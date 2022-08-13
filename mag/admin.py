from django.contrib import admin

from .models import Number, Block, Material

class NumberAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_display_links = ('name', 'published')
    search_fields = ('name', )
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'spell', 'number')
    list_display_links = ('name', 'spell','number')
    search_fields = ('name', 'number')
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'auth', 'block', 'number')
    list_display_links = ('name', 'auth','block', 'number')
    search_fields = ('name', 'auth', 'block')
admin.site.register(Number, NumberAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Material, MaterialAdmin)
