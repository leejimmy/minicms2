from django.contrib import admin
from .models import Column,Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','pub_date','update_time',)

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name','slug','info','nav_display','home_display')

admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)