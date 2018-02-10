from django.contrib import admin

from .models import TDinfo

# Register your models here.

admin.site.site_header = 'TDinfo故障信息系统'
admin.site.site_title = 'TDinfo故障信息系统'

class TDinfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','content','pub_date',)
 
 
admin.site.register(TDinfo, TDinfoAdmin)
search_fields = ('title', 'content',)