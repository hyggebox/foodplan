import requests

from bs4 import BeautifulSoup


url = "https://povar.ru/recipes/kartofelnaya_zapekanka_s_farshem-5781.html"

bs4_response = requests.get(url)
bs4_response.raise_for_status()
soup = BeautifulSoup(bs4_response.text, "html.parser")

title = soup.select_one("h1.detailed").text
image_url = soup.select_one(".bigImgBox img")["src"]
instructions = soup.select(".detailed_step_description_big")
recipe_text = " ".join([instr_part.text for instr_part in instructions])

ingredients = soup.select(".detailed_ingredients>li")

print("TITLE", title)
print("IMAGE_URL", image_url)
print("TEXT", recipe_text)

for ingredient in ingredients:
    ingredient_line = ingredient.text
    ingredient_name = ingredient_line.split("—")[0].strip()
    unsplit_amount = ingredient_line.split("—")[1].strip()
    if 'По вкусу' in unsplit_amount:
        amount, unit = None, None
    else:
        amount, unit = unsplit_amount.split(None, 1)

    print("INGR:", ingredient_name, "AMOUNT:", amount, "UNIT:", unit)