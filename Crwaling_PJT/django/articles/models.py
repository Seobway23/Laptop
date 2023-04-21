from django.db import models

# Create your models here.

# title =['N', '종목명','현재가','전일비','등락률','액면가',	'시가총액','상장주식수','외국인비율','거래량','PER','ROE',]

# stock = Stock.object.get()
# stock.article.name


class Stock(models.Model):
    name = models.TextField(primary_key=True)
    # article = models.ForeignKey(Article, on_delete=True,  )
    current_price = models.IntegerField()
    previous_rate = models.IntegerField()
    rate_of_change = models.TextField()
    face_value = models.IntegerField()
    market_capitalization = models.IntegerField()
    listed_stock = models.IntegerField()
    foreigner_ratio = models.FloatField()
    trading_volume = models.TextField()
    per = models.FloatField()
    roe = models.FloatField()

# 모델에서는 models.Model을 쓰는 이유?


class Article(models.Model):
    name = models.ForeignKey(Stock, on_delete=models.CASCADE,)
    number = models.IntegerField()
    title = models.TextField()
    content = models.TextField()