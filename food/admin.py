from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Recipes, UserProfile, Comments



class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'category', 'views', 'published', 'get_photo')
    list_editable = ('category', 'published')
    list_filter = ('category', 'published')
    search_fields = ('name', 'content')
    list_display_links = ('name',)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url if obj.photo else None}" width="75">')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(Comments)
