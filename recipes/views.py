from django.shortcuts import render
from django.urls import reverse

from .models import Recipe


def get_recipe_data(recipe):
    
    return {
        "title": recipe.title,
        "image": recipe.image.url,
        "description": recipe.description,
        "recipe_text": recipe.recipe_text,
        "ingredients": {
            # ???
        }
    }


def render_recipe_page(request):
    recipes = Recipe.objects.all()

    the_first_recipe = recipes[0]
    # data_recipe = get_recipe_data(the_first_recipe)

    # context = get_recipe_data(the_first_recipe)

    context = {
        "title": "яичница с сосисками",
        "image": "/media/recipes/eggs_with.jpg",
        "description": "Самое топовое блюдо на завтрак! Витаминный заряд!",
        "recipe_text": "Тут долгое описание приготовления! Бла бла Бла бла Бла бла Бла бла Бла бла Бла бла",
        "ingredients": {
            "яйцо": "2 шт",
            "сосиски": "3 шт"
        },
        "calories": "250"
    }

    return render(request, 'main_recipe.html', context=context)
