from django.contrib import admin

# Register your models here.
from app.models import *

class CustomBooks(admin.ModelAdmin):
    list_display=['Section','Book_name','Auther']
    list_display_links=['Book_name']
    list_per_page=3
    list_editable=['Auther']
    list_filter=['Section',]
    search_fields=['Book_name']


admin.site.register(Liabrary)
admin.site.register(Books,CustomBooks)