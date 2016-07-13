# -*- coding: utf-8 -*-
APP_NAME="cda_downloader"
CONFIG_JSON_FILES_FILE = "files.json"
APP_LOCK=False
TITLE_REGEX = "<title.*?>(.+?)</title>"
MP4_FILE_REGEX = "'(.+?)'"
CHROMEDRIVER_PATH="lib/chromedriver"
POLISH_CHARS = {
    "ą".decode('utf8'):"a",
    "ł".decode('utf8'):"l",
    "ę".decode('utf8'):"e",
    "ś".decode('utf8'):"s",
    "ż".decode('utf8'):"z",
    "ź".decode('utf8'):"z",
    "ó".decode('utf8'):"o",
    "ć".decode('utf8'):"c",
    "ń".decode('utf8'):"n"
}
MP4_FILE_EXTENSION = ".mp4"
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Cookie': 'cookieinfo=1; __gfp_64b=TDWA.YHhp85AXk6WEyU815noie1brwFNRndh5t0gyBj.K7; ibbid=BBID-01-01242201350818085; 2015GoldbachTrue_2=4; styczen2016artbrick-1_2=2; styczen2016artbrick-2_2=1; styczen2016artbrick-3_2=1; styczen2016artbrick-4_2=1; styczen2016artbrick_2=5; PHPSESSID=aMdy81MZlPAg6Ki9yp1FFUWlBW5; bblpasync=1456061387153; luty2016vipe=1; luty2016vipe_2=1; _gat=1; __utmt=1; _ga=GA1.2.28076971.1449506134; bblosync=1456062149139; axd=100038331235480140; __utma=223312324.28076971.1449506134.1455390954.1456061392.9; __utmb=223312324.9.10.1456061392; __utmc=223312324; __utmz=223312324.1455390954.8.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __nc_l=2045343883300:|; __nc_ws=eyIwNDNELUEyNUUtRTRBMi1BNDBDLTFaTWFPRyI6eyJ2YyI6M30sIkU0RjgtMzg5RS1FOTdELTdFNEUtMVpNeTF1Ijp7InZjIjoyfX0=; vasty=3',
'Connection': 'keep-alive'}
