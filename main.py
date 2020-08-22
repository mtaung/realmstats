from realmeye import scraper

url = 'https://www.realmeye.com/recent-deaths'
trade_url = 'https://www.realmeye.com/recent-offers'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

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