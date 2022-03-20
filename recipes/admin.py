from django.contrib import admin

from recipes.models import (
    MealTag, Unit, RestrictTag, Ingredient, Recipe, AmountIngredients,
    SubscriptionTimeInterval, Subscription)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unit')


class RecipeInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 2


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'get_meals', 'get_restrict_tags', 'get_ingredients')
    list_filter = ['meals', 'restrict_tags',]
    inlines = [RecipeInline]

    def get_meals(self, obj):
        return obj.get_meals()

    get_meals.short_description = 'Категории блюд'

    def get_restrict_tags(self, obj):
        return obj.get_restrict_tags()

    get_restrict_tags.short_description = 'Ограничения меню'

    def get_ingredients(self, obj):
        return obj.get_ingredients()

    get_ingredients.short_description = 'Ингредиенты'


@admin.register(AmountIngredients)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    search_fields = ['ingredient', 'recipe']
    list_editable = ['amount']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'get_user_email', 'period', 'persons_num',
                    'get_meals', 'get_restrict_tags')
    list_editable = ['period', 'persons_num']

    def get_user_name(self, obj):
        return obj.get_user_name()

    get_user_name.short_description = 'Имя'

    def get_user_email(self, obj):
        return obj.get_user_email()

    get_user_email.short_description = 'Email'

    def get_meals(self, obj):
        return obj.get_meals()

    get_meals.short_description = 'Категории блюд'

    def get_restrict_tags(self, obj):
        return obj.get_restrict_tags()

    get_restrict_tags.short_description = 'Ограничения меню'


@admin.register(SubscriptionTimeInterval)
class SubscriptionTimeIntervalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    list_editable = ['price']


admin.site.register(RestrictTag)
admin.site.register(Unit)
admin.site.register(MealTag)
