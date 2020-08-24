# realmstats

**realmstats** is a simple python based tool to grab data from realmeye's *recent* pages. This data is stored in a sqlite database. 

## Dependencies:
* sqlalchemy
* requests
* beautifulsoup4

## Usage:

Please generate and use your own useragents before running `main.py`. Try to use conservative query intervals, as you may end up generating duplicate entries. The parameters already used in `main.py` will generate occassional duplicates that are easily cleaned in SQL.