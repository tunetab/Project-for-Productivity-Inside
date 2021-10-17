from django.contrib import admin

# Register your models here.

from .models import Type, Recipe, Author

admin.site.register(Type)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pub_date", "title", "display_type", "status")
    list_filter = ("pub_date", "status")

admin.site.register(Recipe, RecipeAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("nickname", "status")

admin.site.register(Author, AuthorAdmin)