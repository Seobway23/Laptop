import csv, json
from bs4 import BeautifulSoup
import requests


base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

name = input("검색종목을 입력하세요 : ")
keyword=  name + "주식"
search_url = base_url + keyword

# 서버 겟 요청보내면 응답 받음 d
r = requests.get(search_url)
#html 넣고, parser 분석
soup = BeautifulSoup(r.text, "html.parser")

#띄어쓰기는 _로 교체시키기
keyword= keyword.replace(" ", "_")

title = ["순번", "이름", "제목", "내용"]

items = soup.select(".news_tit")
contents = soup.select(".api_txt_lines.dsc_txt_wrap")

crawl_data = []
# row 가져와서 하나씩 저장
for i in range(len(items)):
    item = items[i].text
    content = contents[i].text
    crawl_datum = {
    "순번":i+1,
    "이름":name,
    "제목":item,
    "내용":content,
    }
    crawl_data.append(crawl_datum)

json_string = json.dumps(crawl_data, ensure_ascii=False, indent=4)
with open("crawled_data.json", "w", encoding="utf-8") as f:
    f.write(json_string)
