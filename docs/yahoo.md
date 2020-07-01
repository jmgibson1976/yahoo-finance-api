# YAHOO

This document details the methods for collecting urls used to build this API.

## Gathering the Urls

* Using web dev tools supplied by browser, switch to Network tab, and load (https://finance.yahoo.com)
* Right click on first entry (original GET / ) and choose 'Save All AS HAR'
* Put file into data directory at root of project
* Run file through appropriate parser found in /Data/Utils/Parsers
    
    * edit parser, update file_name to match file in data directory
    * cd data/utils/parsers && python3 parseYahooFinanceLinksFromHarCapture.py

* Save the output links to a text file for later use. (ex: finance.yahoo.com.txt)