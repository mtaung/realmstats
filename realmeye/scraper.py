from typing import List
import requests
import bs4
from bs4 import BeautifulSoup as bs


def soupify_html(
    url: str, 
    headers: dict,
) -> bs:

    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser") 

    return soup


def save_soup(
    filename: str, 
    soup: bs,
) -> None:
    
    with open(filename, "w", encoding='utf-8') as file:
        file.write(str(soup.prettify()))   

    return None


def get_table(
    soup: bs,
) -> bs4.element.Tag:
    table = soup.body.find('table', {'id': 'd'})

    return table


def parse_deaths_table(
    table: bs4.element.Tag,
    skip_private: bool = True,
)-> list:

    rows = table.findChildren(['tr'])
    characters = []

    for row in rows[1:100]:
        cols = row.find_all('td')
        cols = [element.text.strip() for element in cols]

        # We don't want to store/handle empty rows
        if cols[1] == 'Private':
            continue

        items = row.find_all('span', {'class':'item'})
        items = [item['title'] for item in items]
        
        character = cols + items
        characters.append(character)

    return characters
