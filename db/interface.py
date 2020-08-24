from datetime import datetime
from sqlalchemy import create_engine, MetaData
import sqlalchemy
import os

def engine(
    meta: sqlalchemy.MetaData = MetaData(),
    db_path: str = 'realmstats.db',
) -> None:
    engine = create_engine('sqlite:///' + db_path)
    meta.create_all(engine)
    return engine


def insert_death(
    death: list, 
    table: sqlalchemy.Table,
    engine: sqlalchemy.engine,
) -> None:
    try:
        backpack_bool = True if death[4][4] else False
    except IndexError:
        backpack_bool = False

    insertion = table.insert().values(
        user = death[0],
        datetime = death[1],
        base_fame = death[2],
        total_fame = death[3],
        weapon = death[4][0],
        secondary = death[4][1],
        armour = death[4][2],
        ring = death[4][3],
        backpack = backpack_bool,
        maxed_stats = int(death[5][0]),
        killed_by = death[6],
    )

    with engine.connect() as connection:
        result = connection.execute(insertion)
    return None


def insert_offer(
    offer: list, 
    table: sqlalchemy.Table,
    engine: sqlalchemy.engine,
) -> None:

    insertion = table.insert().values(
        user = offer[-1],
        selling = ','.join(offer[0]),
        buying = ','.join(offer[1]),
        quantity = offer[2],
        datetime = offer[3], 
    )

    with engine.connect() as connection:
        result = connection.execute(insertion)
    return None
