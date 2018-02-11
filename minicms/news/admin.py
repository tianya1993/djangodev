from django.contrib import admin

from .models import Column, Article

# Register your models here.

admin.site.site_header = 'Minicms内容管理系统'
admin.site.site_title = 'Minicms内容管理系统'

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro',)
    search_fields = ('name', 'slug', 'intro',)
    #list_filter = ('published',)
 	
 
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'content','author', 'pub_date', 'update_time')
	search_fields = ('title', 'content','slug','pub_date', 'update_time')
    #list_filter = ('published',)#提交状态筛选
	empty_value_display = '-empty-'
	list_filter = ('pub_date',)#时间筛选
	date_hierarchy = 'pub_date' #排序接受的是个字符串
	ordering = ('-pub_date',)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)



