from realmeye import scraper

url = 'https://www.realmeye.com/recent-deaths'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

if __name__ == "__main__":
    sample = scraper.soupify_html(url, headers)
    save = scraper.save_soup("example.html", sample)

    table = sample.body.find('table', {'id': 'd'})             
    save = scraper.save_soup("table.html", table)
