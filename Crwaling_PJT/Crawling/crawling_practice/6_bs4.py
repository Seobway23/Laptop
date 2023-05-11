import requests
from bs4   import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8"
requests = requests.get(url)
requests.raise_for_status()

#lxml
# 스크래핑하기 위해, lxml은 구문을 분석하기 위한 parser

soup = BeautifulSoup(requests.text,'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.div)
# print(soup.a.attrs) # 속성 정보 출력
# print(soup.a["href"])

#print(soup)

# # h3태그 안의 class가 ~~인 거 찾아줘
#print(soup.find("h3", attrs ={"class":"WeekdayMainView__heading--tHIYj"})) 
rank1 = soup.find("div", attrs ={"class":"wikipedia-ko news-header"})

print(rank1.next_sibling)   # 친구들 -> .next_sibling
print(rank1.parent)         # 부모 클래스 .parent

print(rank1.find_next_siblings("li"))
print(111111111111111111)

print(rank1.find_previous_siblings)