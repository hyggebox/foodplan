from django.contrib import admin

from recipes.models import (
    Meal, Unit, Subscription, Ingredient, Recipe, AmountIngredients,
    SubscriptionTimeInterval, Specific)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    ...


@admin.register(Unit)
class MealAdmin(admin.ModelAdmin):
    ...


@admin.register(SubscriptionTimeInterval)
class MealAdmin(admin.ModelAdmin):
    ...

@admin.register(Ingredient)
class MealAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class MealAdmin(admin.ModelAdmin):
    ...

@admin.register(AmountIngredients)
class MealAdmin(admin.ModelAdmin):
    ...