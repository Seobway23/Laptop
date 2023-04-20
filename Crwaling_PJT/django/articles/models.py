from django.db import models

# Create your models here.
class Article(models.Model):
    number = models.IntegerField()
    name = models.TextField()
    title = models.TextField()
    content = models.TextField()


# title =['N', '종목명','현재가','전일비','등락률','액면가',	'시가총액','상장주식수','외국인비율','거래량','PER','ROE',]

class Stock(models.Model):
    Name = models.TextField()
    Current_price = models.IntegerField()
    Previous_rate = models.IntegerField()
    Rate_of_change = models.TextField()
    Face_value = models.IntegerField()
    Market_capitalization = models.IntegerField()
    listed_stock = models.IntegerField()
    Foreigner_ratio = models.FloatField()
    Trading_volume = models.TextField()
    PER = models.FloatField()
    ROE = models.FloatField()

# 모델에서는 models.Model을 쓰는 이유?