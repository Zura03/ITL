from django.contrib import admin
from .models import CategoryModel, PageModel
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('index', 'name')
    
admin.site.register(models.CategoryModel, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('index', 'category', 'title')
    
admin.site.register(models.PageModel, PageAdmin)


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'salary')
    
admin.site.register(models.EmpModel, EmpAdmin)