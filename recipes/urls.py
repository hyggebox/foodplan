from django.urls import path


from .views import render_recipe_page


urlpatterns = [
    path('recipe/<int:id>', render_recipe_page, name='render_recipe_page'),
]
