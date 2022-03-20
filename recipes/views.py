from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Recipe, User, Subscription


def select_recipe(subscription):
    persons_num = subscription.persons_num
    restrictions = subscription.restrict_tags.all()
    meals = subscription.meals.all()
    if restrictions:
        subscription_recipe = Recipe.objects.restrictions(restrictions).meals(
            meals).first()
    else:
        subscription_recipe = Recipe.objects.meals(meals).first()
    return subscription_recipe, persons_num


@login_required(login_url='/')
def render_recipe_page(request, sub_id):

    try:
        subscription = Subscription.objects.get(pk=sub_id)
    except Subscription.DoesNotExist:
        return HttpResponse(f'Подписки с id {sub_id} не найдено')

    users_recipe, persons_num = select_recipe(subscription)

    if not users_recipe:
        return HttpResponse('По вашим запросам рецептов не найдено')
        # return HttpResponseRedirect('/sorry')


    context = {
        "title": users_recipe.title,
        "image": users_recipe.image.url,
        "description": users_recipe.description,
        "recipe_text": users_recipe.recipe_text,
        "ingredients": users_recipe.ingredient_amount.all(),
        "calories": users_recipe.calories,
        "persons_num": persons_num
    }

    return render(request, 'main_recipe.html', context=context)
