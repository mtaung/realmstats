from typing import List, Any
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import requests
import bs4


def soupify_html(
    url: str, 
    headers: dict,
) -> bs:

    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser") 
    
    return soup


def save_soup(
    filename: str, 
    soup: Any,
) -> None:
    
    with open(filename, "w", encoding='utf-8') as file:
        file.write(str(soup.prettify()))   

    return None


def get_table(
    soup: bs,
) -> bs4.element.Tag:
    table = soup.body.find('table', {'id': 'e'})
    
    return table


def parse_deaths_table(
    table: bs4.element.Tag,
    skip_private: bool = True,
) -> list:

    rows = table.findChildren(['tr'])
    characters = []

    for row in rows[1:100]:
        
        cols = row.find_all('td')
        cols = [element.text.strip() for element in cols]

        # We don't want to store/handle empty rows
        if cols[1] == 'Private':
            continue

        user = cols[1]
        base_fame = cols[3]
        total_fame = cols[4]
        maxed_stats = cols[6]
        killed_by = cols[7]

        datetime = cols[2].replace('T', ' ')[:-1] 
        datetime = dt.strptime(datetime, '%Y-%m-%d %H:%M:%S')

        items = row.find_all('span', {'class':'item'})
        items = [item['title'] for item in items]
        
        character = [
            user, 
            datetime,
            base_fame,
            total_fame,
            items,
            maxed_stats, 
            killed_by,
            ]
        characters.append(character)

    return characters


def parse_offers_table(
    table: bs4.element.Tag,
    skip_private: bool = True,
) -> list:

    rows = table.findChildren(['tr'])
    offers = []
    for row in rows[1:100]:
        selling = row.findChildren(['td'])[0]
        selling_items = parse_offer_items(selling) 

        buying = row.findChildren(['td'])[1]
        buying_items = parse_offer_items(buying) 

        quantity = row.findChildren(['td'])[2].text

        datetime = row.findChildren(['td'])[3].text
        datetime = dt.strptime(datetime, '%Y-%m-%d %H:%M:%S')
        
        user = row.findChildren(['td'])[5].text

        offer = [
            selling_items, 
            buying_items, 
            quantity, 
            datetime, 
            user,
            ]
        offers.append(offer) 
        
    return offers


def parse_offer_items(
    row: bs4.element.Tag
) -> list:

    items = row.find_all('span', {'class':'item'})
    items = [item['data-item'] for item in items]
    return items
