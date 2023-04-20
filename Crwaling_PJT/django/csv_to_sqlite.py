'''
df = pandas.read_csv(csvfile)
df.to_sql(table_name, conn, if_exists='append', index=False)

나중에 되는지 확인하기
'''
def str_to_int(N):
    if N == 'N/A':
        return 0 
    try:
        Num = N.replace(',','')
        Num_int = float(Num)
        return Num_int
    except:
        return N

'-3,469.57'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawl_pjt.settings")

from django.conf import settings

#이게 처음 DB에 없으면 오류가 남 왜 그런지는 잘 모르겠음
# settings.configure(INSTALLED_APPS=['articles'])



import django
django.setup()

from articles.models import Stock
import csv

# title =['N', '종목명','현재가','전일비','등락률','액면가',	'시가총액','상장주식수','외국인비율','거래량','PER','ROE',]

# Name = models.TextField()
# Current_price = models.IntegerField()
# Previous_rate = models.IntegerField()
# Rate_of_change = models.IntegerField()
# Face_value = models.IntegerField()
# Market_capitalization = models.IntegerField()
# listed_stock = models.IntegerField()
# Foreigner_ratio = models.IntegerField()
# Trading_volume = models.IntegerField()
# PER = models.IntegerField()
# ROE = models.IntegerField()

#여기서 f 는 str 형태로 나옴
with open("KOSPI200.csv", "r", encoding="utf-8", newline="") as f:
    data = csv.reader(f)
    for datum in data:
        #print(i)
        #print(datum)
        stock = Stock(
            Name=datum[1],
            Current_price = str_to_int(datum[2]),
            Previous_rate = str_to_int(datum[3]),
            Rate_of_change = str_to_int(datum[4]),
            Face_value = str_to_int(datum[5]),
            Market_capitalization = str_to_int(datum[6]),
            listed_stock = str_to_int(datum[7]),
            Foreigner_ratio = str_to_int(datum[8]),
            Trading_volume = str_to_int(datum[9]),
            PER = str_to_int(datum[10]),
            ROE = str_to_int(datum[11]),
        )
        stock.save()

'''
1,삼성전자,"65,000",500,-0.76%,100,"3,880,359","5,969,783",51.58,"5,819,281",8.07,17.07,

'''
    #csv에서는 dicreader를 사용하여 딕셔너리화함??
