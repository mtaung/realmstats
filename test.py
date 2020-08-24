from realmeye import scraper
from db import interface
from db.tables import deaths, trades

url = 'https://www.realmeye.com/recent-deaths'
trade_url = 'https://www.realmeye.com/recent-offers'
headers = {'User-Agent': 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'}

if __name__ == "__main__":
    sample = scraper.soupify_html(url, headers)
    scraper.save_soup("deaths.html", sample)

    table = scraper.get_table(sample)
    scraper.save_soup("deaths_table.html", table)

    characters = scraper.parse_deaths_table(table)

    sales = scraper.soupify_html(trade_url, headers)
    scraper.save_soup('offers.html', sales)
    trade_table = scraper.get_table(sales)
    scraper.save_soup('offers_table.html', trade_table)

    offers = scraper.parse_offers_table(trade_table)

    engine = interface.engine()
    for character in characters:
        interface.insert_death(character, deaths, engine)

    for offer in offers:
        interface.insert_offer(offer, trades, engine)
