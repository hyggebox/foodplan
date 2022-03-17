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
