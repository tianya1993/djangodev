from django.contrib import admin

from .models import Userinfo
 
admin.site.site_header = 'Domcms'
admin.site.site_title = 'Domcms'
class UserinfoAdmin(admin.ModelAdmin):
	list_display = ('username','sex','email',ßß)
    #list_display = ('username','sex','email','pub_date','update_time',)

 
admin.site.register(Userinfo,UserinfoAdmin)


