from django.contrib import admin

# Register your models here.

from app.models import *

class CustmizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['email']
    list_editable=['url']
    list_filter=('url',)
    list_per_page=3

admin.site.register(Topic)

admin.site.register(WebPage,CustmizeWebpage)

admin.site.register(AccessRecord)