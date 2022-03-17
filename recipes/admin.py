from django.contrib import admin

from recipes.models import (
    MealTag, Unit, RestrictTag, Ingredient, Recipe, AmountIngredients,
    SubscriptionTimeInterval, Subscription)


@admin.register(MealTag)
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


@admin.register(RestrictTag)
class MealAdmin(admin.ModelAdmin):
    ...

@admin.register(Subscription)
class MealAdmin(admin.ModelAdmin):
    ...
