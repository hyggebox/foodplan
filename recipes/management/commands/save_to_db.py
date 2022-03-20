import json
import os

from django.core.management.base import BaseCommand
from django.core.files import File
from urllib import request

from recipes.models import Recipe, Unit, Ingredient, MealTag, RestrictTag


MEALS = ['На завтрак', 'На обед', 'На ужин', 'Десерты', 'Праздничное меню']
RESTRICTIONS = ['Вегетарианские блюда', 'Диетические блюда', 'Сыроедческие блюда']



def add_meal_tag(correlation, categories, recipe):
    category, meal_tag = correlation
    if category in categories:
        tag = MealTag.objects.get(meal=meal_tag)
        recipe.meals.add(tag)


def add_restriction(correlation, categories, recipe):
    category, restriction_tag = correlation
    if category in categories:
        tag = RestrictTag.objects.get(tag=restriction_tag)
        recipe.restrict_tags.add(tag)


def main():
    with open('recipes.json', encoding='utf8') as json_file:
        recipes = json.load(json_file)

    # Save Meals
    for meal in MEALS:
        MealTag.objects.get_or_create(meal=meal)

    # Save Restrictions
    for restriction in RESTRICTIONS:
        RestrictTag.objects.get_or_create(tag=restriction)

    # Save Units
    for recipe in recipes.values():
        ingredients = recipe['ingredients']
        for ingredient in ingredients:
            unit = ingredient['unit']
            if unit:
                Unit.objects.get_or_create(name=unit)

    # Save Ingredients
    for recipe in recipes.values():
        ingredients = recipe['ingredients']
        for ingredient in ingredients:
            ingredient_unit = Unit.objects.get(name=ingredient['unit']) if \
            ingredient['unit'] else None
            Ingredient.objects.get_or_create(
                product_name=ingredient['name'],
                unit=ingredient_unit
            )

    # Save Recipes
    Recipe.objects.all().delete()
    for recipe in recipes.items():
        new_recipe = Recipe(
            title=recipe[0],
            description=recipe[1]['description'],
            recipe_text=recipe[1]['text'],
            calories=recipe[1]['cal']
        )

        response = request.urlretrieve(recipe[1]['img_url'])
        new_recipe.image.save(
            os.path.basename(recipe[1]['img_url']),
            File(open(response[0], 'rb'))
        )

        recipe_categories = recipe[1]['categories']
        recipe_ingredients = recipe[1]['ingredients']
        recipe_portions = recipe[1]['portions']

        new_recipe.save()

        categories_meals_correlations = [('На завтрак', MEALS[0]),
                                         ('На обед', MEALS[1]),
                                         ('На ужин', MEALS[2]),
                                         ('Сладкое', MEALS[3]),
                                         ('Десерты', MEALS[3]),
                                         ('На праздничный стол', MEALS[4])]
        categories_restrictions_correlations = [
            ('Вегетарианское питание', RESTRICTIONS[0]),
            ('Веганские блюда', RESTRICTIONS[0]),
            ('Диетическое питание', RESTRICTIONS[1]),
            ('Рецепты сыроедения', RESTRICTIONS[2]),
        ]
        for correlation in categories_meals_correlations:
            add_meal_tag(correlation, recipe_categories, new_recipe)

        for correlation in categories_restrictions_correlations:
            add_restriction(correlation, recipe_categories, new_recipe)

        for ingredient in recipe_ingredients:
            recipe_ingredient = Ingredient.objects.filter(
                product_name=ingredient['name'],
                unit__name=ingredient['unit']
            ).first()
            new_recipe.ingredients.add(recipe_ingredient)
            if ingredient['amount']:
                ing_amount = new_recipe.ingredient_amount.filter(
                    ingredient__product_name=recipe_ingredient).first()
                ing_amount.amount = round(ingredient['amount'] / recipe_portions, 2) \
                    if recipe_portions else ingredient['amount']
                ing_amount.save()

    all_recipes = Recipe.objects.all()
    for recipe in all_recipes:
        if recipe.meals.count() == 0:
            recipe.delete()


class Command(BaseCommand):

    def handle(self, *args, **options):
        main()
