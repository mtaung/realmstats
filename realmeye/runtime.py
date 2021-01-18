from realmeye.scraper import soupify_html, get_table, parse_deaths_table, parse_offers_table
from db import interface 
from db.tables import deaths, trades
from time import sleep
from typing import Callable
import datetime as dt
import logging
import sqlalchemy
import random
import logging

logging.basicConfig(level=logging.INFO, filename='debugging.log')


def query_deaths(
    url: str,
    headers: dict,
    engine: sqlalchemy.engine,
) -> None:

    death_samples = soupify_html(url, headers)
    death_samples = get_table(death_samples)
    death_samples = parse_deaths_table(death_samples)
    
    for death in death_samples:
        interface.insert_death(death, deaths, engine)


def query_offers(
    url: str,
    headers: dict,
    engine: sqlalchemy.engine,
) -> None:

    offer_samples = soupify_html(url, headers)
    offer_samples = get_table(offer_samples)
    offer_samples = parse_offers_table(offer_samples)

    for offer in offer_samples:
        interface.insert_offer(offer, trades, engine)


def timed_miner(
    func: Callable,
    interval: int, 
    url: str,
    headers: dict,
    engine: sqlalchemy.engine,
) -> None:

    def while_func():
        while True:
            try:
                func(url, headers, engine)
                naptime = interval + random.uniform(0, 30)
                logging.info(f'{dt.datetime.now()}: {func} ran, waiting {naptime}s.')
                sleep(naptime)
            except Exception as excep:
                logging.info(f'{dt.datetime.now()}: {func} failed to run. {excep}')


    return while_func