# realmstats

**realmstats** is a simple python based tool to grab data from realmeye's *recent* pages. This data is stored in a sqlite database. 

## Dependencies:
* sqlalchemy
* requests
* beautifulsoup4

## Usage:

Please generate and use your own useragents before running `main.py`. Try to use conservative query intervals, as you may end up generating duplicate entries. The parameters already used in `main.py` will generate occassional duplicates that are easily cleaned in SQL.

## TODO: 

* The actual *stats* part of *realmstats*, once some good amount of data has been collected.
* SQL tools, including duplicate cleanup and some interfacing with common modalities like pandas or csv. 
* More thorough logging. 

## Disclaimer:

This code was written over the course of a couple of days as a demonstration to assist teaching of *"real world"* python to a young highschool student. Readability was prioritised first and foremost and no guarantees of security, stability, or optimality are ensured.