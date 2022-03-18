from django.contrib import admin

from recipes.models import (
    MealTag, Unit, RestrictTag, Ingredient, Recipe, AmountIngredients,
    SubscriptionTimeInterval, Subscription)


@admin.register(MealTag)
class MealAdmin(admin.ModelAdmin):
    ...


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    ...


@admin.register(SubscriptionTimeInterval)
class SubscriptionTimeInterval(admin.ModelAdmin):
    ...

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unit')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'get_meals', 'get_restrict_tags', 'get_ingredients')


@admin.register(AmountIngredients)
class AmountAdmin(admin.ModelAdmin):
    ...


@admin.register(RestrictTag)
class RestrictTagAdmin(admin.ModelAdmin):
    ...

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'period', 'persons_num', 'get_meals', 'get_restrict_tags')
