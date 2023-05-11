import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawl_pjt.settings")

import django
django.setup()

from articles.models import Article
import json

import csv
import requests
from bs4 import BeautifulSoup

# 

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?&page='

filename = "KOSPI200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline 은 줄바꿈 엔터 없애줌
writer = csv.writer(f)

# title =['N', '종목명','현재가','전일비','등락률','액면가',	'시가총액','상장주식수','외국인비율','거래량','PER','ROE',]
# writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns)<= 1: #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] # strip() -> 문자열의 시작과 끝에 주어진 문자가 아닌 것을 제거 (예를 들어 띄어 쓰기) 
        writer.writerow(data)
        