# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Blog,Category,Tag,Image

class BlogAdmin(admin.ModelAdmin):
    list_display = ['caption','slug','id','counts','category','publish_time']
    list_filter = ['caption']
    prepopulated_fields = {'slug':('caption',)}
    data_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags','images')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','description','image']


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Image,ImageAdmin)
