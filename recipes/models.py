from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    """ теги аллергий"""
    meal = models.CharField('Тэги для пищи', max_length=20)

    class Meta:
        verbose_name = 'Тэг для пищи'
        verbose_name_plural = 'Тэги для пищи'

    def __str__(self):
        return self.meal


class Unit(models.Model):
    name = models.CharField('Мера измерения продукта', max_length=20)

    class Meta:
        verbose_name = 'Мера продукта'
        verbose_name_plural = 'Меры продуктов'

    def __str__(self):
        return self.name


class SubscriptionTimeInterval(models.Model):
    time_intervals = models.PositiveIntegerField(
        'временные интервалы для подписки в месяцах')

    class Meta:
        verbose_name = 'временной интервал для подписки'
        verbose_name_plural = 'временные интервалы для подписки'

    def __str__(self):
        return f'Интервал {self.time_intervals} месяцев'


class Ingredient(models.Model):
    """виды продуктов для рецепта"""
    product_name = models.CharField('Название продукта', max_length=20)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        verbose_name='Меры продуктов',
        null=True,)

    class Meta:
        verbose_name = 'Тип ингредиента'
        verbose_name_plural = 'Тип ингредиентов'

    def __str__(self):
        return self.product_name


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=50)
    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True,
        verbose_name='Изображение к рецепту')
    description = models.TextField(
        blank=True,
        verbose_name='Краткое описание', )
    recipe_text = models.TextField(
        blank=True,
        verbose_name='описание приготовления',)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='AmountIngredients',
        verbose_name='Игредиенты для рецепта',)
    meal = models.ManyToManyField(Tag, verbose_name='Приём пищи')
    calories = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class AmountIngredients(models.Model):
    """ингридиенты и их количество для рецепта"""
    ingredient = models.ForeignKey(
        Ingredient,
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


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Пользователь',)
    time_intervals = models.ForeignKey(
        SubscriptionTimeInterval,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Время подписки')
    tag = models.ManyToManyField(Tag, verbose_name='Название приёма пищи')
    person_quantity = models.PositiveIntegerField('Количество персон', default=1)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    holiday_dinner = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Пользователь {self.user} подписка на {self.time_intervals.time_intervals}'







