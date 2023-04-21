import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawl_pjt.settings")

import django
django.setup()

from articles.models import Article, Stock
import json

with open("crawled_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    #print('data:', data)
    for datum in data:
        #print(datum)
        stock_name = Stock.objects.get(pk =datum['이름'])
        #print(datum)
        article = Article(
            name = stock_name,
            number = datum['순번'],
            title = datum['제목'],
            content = datum['내용']
        )
        article.save()
        #print(article)

    #articles = Article.objects.all()

#이렇게 하니까, article -> DB에 저장됨
