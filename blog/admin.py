from django.contrib import admin

from .models import Dish, Ingredient, Spice

class IngredientsInLine(admin.TabularInline):
    model = Ingredient
    extra = 0

class SpicesInLine(admin.TabularInline):
    model = Spice
    extra = 0

class DishAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of dish?', {'fields': ['dish_name']}),
        ('Category', {'fields': ['kind_of_meal', 'country']}),
        ('How to prepare?', {'fields': ['recipe']}),
        ('Load image', {'fields': ['dish_image']}),
    ]
    inlines = [IngredientsInLine, SpicesInLine]

admin.site.register(Dish, DishAdmin)