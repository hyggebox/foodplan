

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counts', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Ингридиент для рецепта',
                'verbose_name_plural': 'Ингридиенты для рецепта',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20, verbose_name='Название продукта')),
            ],
            options={
                'verbose_name': 'Тип ингредиента',
                'verbose_name_plural': 'Тип ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='MealTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=20, verbose_name='тэги приёмов пищи')),
            ],
            options={
                'verbose_name': 'тэг приёмов пищи',
                'verbose_name_plural': 'тэги приёмов пищи',
            },
        ),
        migrations.CreateModel(
            name='RestrictTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тэги для пищи')),
            ],
            options={
                'verbose_name': 'Тэг ограничений',
                'verbose_name_plural': 'Тэги ограничений',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionTimeInterval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_intervals', models.PositiveIntegerField(verbose_name='временные интервалы для подписки в месяцах')),
            ],
            options={
                'verbose_name': 'временной интервал для подписки',
                'verbose_name_plural': 'временные интервалы для подписки',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Мера измерения продукта')),
            ],
            options={
                'verbose_name': 'Мера продукта',
                'verbose_name_plural': 'Меры продуктов',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_quantity', models.PositiveIntegerField(default=1, verbose_name='Количество персон')),
                ('meal', models.ManyToManyField(blank=True, to='recipes.mealtag', verbose_name='приём пищи')),
                ('restrict_tag', models.ManyToManyField(blank=True, to='recipes.restricttag', verbose_name='ограничения')),
                ('time_intervals', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='recipes.subscriptiontimeinterval', verbose_name='Время подписки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название рецепта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Изображение к рецепту')),
                ('description', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('recipe_text', models.TextField(blank=True, verbose_name='описание приготовления')),
                ('calories', models.PositiveIntegerField(default=1)),
                ('allergic', models.ManyToManyField(to='recipes.restricttag', verbose_name='Тэг алергичного продукта')),
                ('ingredients', models.ManyToManyField(through='recipes.AmountIngredients', to='recipes.ingredient', verbose_name='Игредиенты для рецепта')),
                ('meal', models.ManyToManyField(to='recipes.mealtag', verbose_name='Приём пищи')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.unit', verbose_name='Меры продуктов'),
        ),
        migrations.AddField(
            model_name='amountingredients',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient', verbose_name='ингредиент'),
        ),
        migrations.AddField(
            model_name='amountingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='рецепт'),
        ),
    ]
