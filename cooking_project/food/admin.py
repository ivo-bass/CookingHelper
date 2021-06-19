from django.contrib import admin

from cooking_project.food.models import Meal, Coarse, Food, Garnish


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('type', 'start_time', 'end_time',)


@admin.register(Coarse)
class CoarseAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


@admin.register(Garnish)
class GarnishAdmin(admin.ModelAdmin):
    list_display = ('name',)

