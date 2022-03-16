import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_recipes_links(category_url):
    response = requests.get(category_url)
    response.raise_for_status()
    category_soup = BeautifulSoup(response.text, 'html.parser')

    recipes_links = category_soup.select('a.listRecipieTitle')
    return [link['href'] for link in recipes_links]


if __name__ == '__main__':
    domain = "https://povar.ru/"
    category = '/list/goryachie_bliuda/'

    recipes_urls = get_recipes_links(urljoin(domain, category))
    for url in recipes_urls:
        response = requests.get(urljoin(domain, url))
        response.raise_for_status()
        recipe_soup = BeautifulSoup(response.text, 'html.parser')

        title = recipe_soup.select_one('h1.detailed').text
        image_url = recipe_soup.select_one('.bigImgBox img')['src']
        instructions = recipe_soup.select('.detailed_step_description_big')
        recipe_text = ' '.join([instr_part.text for instr_part in instructions])

        ingredients = recipe_soup.select('.detailed_ingredients>li')

        print('TITLE', title)
        print('IMAGE_URL', image_url)
        print('TEXT', recipe_text)

        for ingredient in ingredients:
            ingredient_line = ingredient.text
            ingredient_name = ingredient_line.split('—')[0].strip()
            unsplit_amount = ingredient_line.split('—')[1].strip()
            if 'По вкусу' in unsplit_amount:
                amount, unit = None, None
            else:
                amount, unit = unsplit_amount.split(None, 1)

            print('INGR:', ingredient_name, 'AMOUNT:', amount, 'UNIT:', unit)

        print('')
