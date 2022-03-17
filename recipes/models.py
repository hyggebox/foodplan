from django.db import models


class Meal(models.Model):
    """ завтрак, обед, ужин, десерт"""
    meal = models.CharField('Приём пищи', max_length=20)

    class Meta:
        verbose_name = 'Приём пищи'
        verbose_name_plural = 'Приём пищи'

    def __str__(self):
        return self.meal


class Units(models.Model):
    name = models.CharField('Мера измерения продукта', max_length=20)

    class Meta:
        verbose_name = 'Мера продукта'
        verbose_name_plural = 'Меры продуктов'

    def __str__(self):
        return self.name


class SubscriptionTimeIntervals(models.Model):
    time_intervals = models.PositiveIntegerField(
        'временные интервалы для подписки')

    class Meta:
        verbose_name = 'временной интервал для подписки'
        verbose_name_plural = 'временные интервалы для подписки'

    def __str__(self):
        return f'интервал {self.time_intervals}'


class Ingredients(models.Model):
    """виды продуктов для рецепта"""
    product_name = models.CharField('Название продукта', max_length=20)
    unit = models.ForeignKey(
        Units,
        on_delete=models.SET_NULL,
        verbose_name='Меры продуктов',
        null=True,)
    calories = models.PositiveIntegerField()
    with_glutogen = models.BooleanField()
    vegetarian_food = models.BooleanField()

    class Meta:
        verbose_name = 'Тип ингредиента'
        verbose_name_plural = 'Тип ингредиентов'

    def __str__(self):
        return self.product_name


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=50)
    image = models.ImageField()
    recipe_text = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    meal = models.ManyToManyField(Meal)


class AmountIngredients(models.Model):
    """ингридиенты и их количество для рецепта"""
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        verbose_name='ингредиент')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='рецепт',)
    counts = models.PositiveSmallIntegerField(
        'Количество',
        default=1)

    class Meta:
        verbose_name = 'Ингридиент для рецепта'
        verbose_name_plural = 'Ингридиенты для рецепта'

    def __str__(self):
        return self.ingredient.product_name






