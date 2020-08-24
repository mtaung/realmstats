from db.tables import deaths
from realmeye.runtime import query_deaths, query_offers
from realmeye import runtime
from db import interface
from multiprocessing import Process

if __name__ == '__main__':
        
    deaths_url = 'https://www.realmeye.com/recent-deaths'
    offers_url = 'https://www.realmeye.com/recent-offers'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    
    engine = interface.engine()

    offers = runtime.timed_miner(query_offers, 60*5, offers_url, headers, engine)
    deaths = runtime.timed_miner(query_deaths, 60*15, deaths_url, headers, engine)
    offers_proc = Process(target=offers)
    deaths_proc = Process(target=deaths)

    offers_proc.start()
    deaths_proc.start()
