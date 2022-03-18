import json
import requests

from bs4 import BeautifulSoup
from functools import reduce
from random import randint
from urllib.parse import urljoin


DOMAIN = 'https://povar.ru/'
ALL_RECIPES_PAGE = '/master/all/'
NUM_PAGES = 10


def get_recipes_links(category_url):
    response = requests.get(category_url)
    response.raise_for_status()
    category_soup = BeautifulSoup(response.text, 'html.parser')
    recipes_links = category_soup.select('a.listRecipieTitle')
    return [link['href'] for link in recipes_links]


def parse_recipe_details(soup, recipe_details):
    title = soup.select_one('h1.detailed').text
    image_url = soup.select_one('.bigImgBox img')['src']
    description = soup.select_one('.detailed_full').text.strip()
    instructions = soup.select('.detailed_step_description_big')
    recipe_text = ' '.join([instr_part.text for instr_part in instructions])

    categories = soup.select('.detailed_tags a')
    clean_categories = [category.text for category in categories]

    portions = soup.select_one('.ingredients_wrapper .detailed_full em').text.split()[2]
    converted_portions = convert_portions(portions)

    ingredients = soup.select('.detailed_ingredients>li')

    recipe_details[title] = {
        'img_url': image_url,
        'description': description,
        'text': recipe_text,
        'categories': clean_categories,
        'ingredients': [],
        'portions': converted_portions,
        'cal': randint(200, 1050)
    }

    for ingredient in ingredients:
        ingredient_line = ingredient.text
        ingredient_name = ingredient_line.split('—')[0].strip()
        unsplit_amount = ingredient_line.split('—')[1].strip()
        if 'По вкусу' in unsplit_amount:
            amount, unit = None, None
        else:
            amount, unit = unsplit_amount.split(None, 1)

        clean_unit = None if not unit else fix_unit(unit.lower())
        clean_amount = None if not amount else convert_amount(amount)

        recipe_details[title]['ingredients'].append({
            'name': ingredient_name,
            'amount': clean_amount,
            'unit': clean_unit
        })
    return recipe_details


def fix_unit(unit):
    match unit:
        case unit if 'килограмм' in unit:
            return 'кг'
        case unit if 'грамм' in unit:
            return 'г'
        case unit if 'стакан' in unit:
            return 'стаканы'
        case unit if 'миллилитр' in unit:
            return 'мл'
        case unit if 'литр' in unit:
            return 'л'
        case unit if 'штук' in unit:
            return 'шт'
        case unit if 'ст. лож' in unit:
            return 'ст.л.'
        case unit if 'чайн' in unit:
            return 'ч.л.'
        case unit if 'штук' in unit:
            return 'шт'
        case unit if 'пучк' in unit:
            return 'пучки'
        case unit if 'ломтик' in unit:
            return 'ломтики'
        case unit if 'банк' or 'банок' in unit:
            return 'банки'
        case unit if 'щепот' in unit:
            return 'щепотки'
        case unit if 'зубч' in unit:
            return 'зубчики'


def convert_amount(parsed_qty):
    if "-" and "/" in parsed_qty:
        split_num = parsed_qty.split("-")[0].split("/")
        converted_gty = round(int(split_num[0]) / int(split_num[1]), 2)
    elif "-" in parsed_qty:
        split_gty = parsed_qty.split("-")[0]
        converted_gty = int(split_gty) if not ',' in split_gty else \
            float(split_gty.replace(",", "."))
    elif "=" in parsed_qty:
        converted_gty = int(parsed_qty.split("=")[0])
    elif "/" in parsed_qty:
        split_num = parsed_qty.split("/")
        converted_gty = round(int(split_num[0]) / int(split_num[1]), 2)
    elif "," in parsed_qty:
        converted_gty = float(parsed_qty.replace(",", "."))
    elif parsed_qty.isdigit():
        converted_gty = int(parsed_qty)
    else:
        converted_gty = None
    return converted_gty


def convert_portions(parsed_portions):
    if parsed_portions.isdigit():
        return int(parsed_portions)
    elif "-" in parsed_portions:
        return int(parsed_portions.split("-")[0])


if __name__ == '__main__':
    recipe_details = {}

    for page in range(1, NUM_PAGES+1):
        recipes_page = reduce(urljoin, [DOMAIN, ALL_RECIPES_PAGE, str(page)])
        recipes_urls = get_recipes_links(recipes_page)

        for url in recipes_urls:
            response = requests.get(urljoin(DOMAIN, url))
            response.raise_for_status()
            recipe_soup = BeautifulSoup(response.text, 'html.parser')
            parse_recipe_details(recipe_soup, recipe_details)

    with open('recipes.json', 'w', encoding='utf8') as file:
        json.dump(recipe_details, file, ensure_ascii=False, indent=4)
