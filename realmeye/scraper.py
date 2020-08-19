import requests
from bs4 import BeautifulSoup as bs


def soupify_html(
    url: str, 
    headers: str,
) -> str:

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