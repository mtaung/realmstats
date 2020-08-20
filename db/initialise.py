from sqlalchemy import create_engine, Table, MetaData, Column, Integer, Float, String, Boolean, DateTime, ForeignKey
import os
import logging

def init(
    db_path: str = 'realmstats.db',
) -> None:
    if not os.path.isfile(db_path):
        engine = create_engine('sqlite:///' + db_path)
        meta.create_all(engine)

if __name__ == '__main__': 

    meta = MetaData()

    deaths = Table(
        'deaths', 
        meta,
        Column('id', String(20), primary_key = True),
        Column('name', String(20)),
        Column('date', DateTime),
        Column('base_fame', Integer),
        Column('total_fame', Integer),
        Column('weapon', String(30)),
        Column('secondary', String(30)),
        Column('armour', String(30)),
        Column('ring', String(30)),
        Column('backpack', Boolean),
        Column('killed_by', String(20)),
    )

    trades = Table(
        'trades',
        meta,
        Column('id', String(20), primary_key = True),
        Column('seller', String(20)),
        Column('selling', String(50)),
        Column('buying', String(50)),
        Column('quantity', Integer),
        Column('datetime', DateTime),
    )

    init()
