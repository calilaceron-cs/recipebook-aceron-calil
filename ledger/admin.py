from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    list_display = ("name", "author", "created_on", "updated_on")
    readonly_fields = ("created_on", "updated_on")
    fields = ("name", "author", "created_on", "updated_on")
    model = Recipe


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
