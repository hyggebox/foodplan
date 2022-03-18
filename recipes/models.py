from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class RestrictTag(models.Model):
    """ограничения по меню"""
    tag = models.CharField('Ограничение по меню', max_length=100)

    class Meta:
        verbose_name = 'Ограничение по меню'
        verbose_name_plural = 'Ограничения по меню'

    def __str__(self):
        return self.tag


class MealTag(models.Model):
    """категория блюда, приём пиши"""
    meal = models.CharField('Приём пищи', max_length=100)

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'

    def __str__(self):
        return self.meal


class Unit(models.Model):
    name = models.CharField('Мера измерения', max_length=100)

    class Meta:
        verbose_name = 'Мера измерения'
        verbose_name_plural = 'Меры измерения'

    def __str__(self):
        return self.name


class SubscriptionTimeInterval(models.Model):
    time_intervals = models.PositiveIntegerField(
        'Период посписки в месяцах')

    class Meta:
        verbose_name = 'Период подписки'
        verbose_name_plural = 'Периоды подписки'

    def __str__(self):
        return f'{self.time_intervals} месяцев'


class Ingredient(models.Model):
    """виды продуктов для рецепта"""
    product_name = models.CharField('Название продукта', max_length=200)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        verbose_name='Мера измерения',
        null=True,)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.product_name


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=200)
    image = models.ImageField(
        upload_to='recipes',
        blank=True,
        null=True,
        verbose_name='Изображение к рецепту')
    description = models.TextField(
        blank=True,
        verbose_name='Краткое описание', )
    recipe_text = models.TextField(
        verbose_name='Описание приготовления',)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='AmountIngredients',
        verbose_name='Ингредиенты в рецепте',)
    meals = models.ManyToManyField(MealTag, verbose_name='Категории блюд')
    restrict_tags = models.ManyToManyField(RestrictTag,
                                           verbose_name='Ограничения в меню',
                                           blank=True)
    calories = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    def get_meals(self):
        return " , ".join([str(meal) for meal in self.meals.all()])

    def get_restrict_tags(self):
        return " , ".join([str(meal) for meal in self.restrict_tags.all()])

    def get_ingredients(self):
        return " , ".join([str(meal) for meal in self.ingredients.all()])


class AmountIngredients(models.Model):
    """ингредиенты и их количество для рецепта"""
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='ингредиент',
        related_name='ingredient_amount')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='рецепт',
        related_name='ingredient_amount')
    amount = models.FloatField('Количество', null=True, blank=True)

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'

    def __str__(self):
        return self.ingredient.product_name


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Пользователь',)
    period = models.ForeignKey(
        SubscriptionTimeInterval,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Длительность подписки')
    restrict_tags = models.ManyToManyField(
        RestrictTag,
        verbose_name='Ограничения',
        blank=True)
    persons_num = models.PositiveIntegerField(
        'Количество персон',
        default=1
    )
    meals = models.ManyToManyField(
        MealTag,
        verbose_name='Категории блюд',
        blank=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Пользователь {self.user} подписка на {self.period}'

    def get_meals(self):
        return " , ".join([str(meal) for meal in self.meals.all()])

    def get_restrict_tags(self):
        return " , ".join([str(meal) for meal in self.restrict_tags.all()])







