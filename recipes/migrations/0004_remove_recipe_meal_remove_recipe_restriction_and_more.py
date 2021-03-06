# Generated by Django 4.0.3 on 2022-03-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_person_quantity_subscription_persons_num_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='restriction',
        ),
        migrations.AddField(
            model_name='recipe',
            name='meals',
            field=models.ManyToManyField(to='recipes.mealtag', verbose_name='Категории блюд'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='restrict_tags',
            field=models.ManyToManyField(to='recipes.restricttag', verbose_name='Ограничения в меню'),
        ),
    ]
