import requests
from bs4   import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8"
requests = requests.get(url)
requests.raise_for_status()

#lxml
# 스크래핑하기 위해, lxml은 구문을 분석하기 위한 parser
soup = BeautifulSoup(requests.text,'lxml')

contents = soup.find_all("div", attrs ={"class":"main-shortcut-item"})

# i = 0
# for content in contents:
#     print(content.get_text())
#     i += 1
#     print(i)


print(contents)