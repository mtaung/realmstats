from sqlalchemy import create_engine, Table, MetaData, Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from db import interface
import os
import logging

meta = MetaData()

deaths = Table(
    'deaths', 
    meta,
    Column('id', Integer, primary_key = True),
    Column('user', String(20)),
    Column('datetime', DateTime),
    Column('base_fame', Integer),
    Column('total_fame', Integer),
    Column('weapon', String),
    Column('secondary', String),
    Column('armour', String),
    Column('ring', String),
    Column('backpack', Boolean),
    Column('maxed_stats', Integer),
    Column('killed_by', String(20)),
)

trades = Table(
    'trades',
    meta,
    Column('id', Integer, primary_key = True),
    Column('user', String(20)),
    Column('selling', String),
    Column('buying', String),
    Column('quantity', Integer),
    Column('datetime', DateTime),
)

interface.engine(meta)
