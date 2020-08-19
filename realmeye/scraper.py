import requests
from bs4 import BeautifulSoup as bs

def scrape_html(
    url: str, 
    headers: str,
) -> str:

    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser") 
    return soup
