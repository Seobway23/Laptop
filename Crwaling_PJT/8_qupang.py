import requests
from bs4   import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=8&backgroundColor="
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'} #headers= 부터 여기까지 한 줄임
requests = requests.get(url, headers=headers)
requests.raise_for_status()
soup = BeautifulSoup(requests.text,'lxml')


#title_list = soup.find_all('a', class_ = 'title') 
#span 태그 안의 class가 title 인 것을 찾아, 변수 title_list에 담는다.

items = soup.find_all("li", attrs = {"class":re.compile("^search-product")})
print(items[0].find("div", attrs = {"class":"name"}).get_text())


#titles = soup.find_all('div', {'class':'ellipsis rank02'})
#titles = soup.find_all('div', {'class':'wrap_song_info'})
# artists = soup.find_all('span', 'checkEllipsis')
#num = soup.find_all('div', 'wrap_song-_info')

# print(len(artists))
# for a in artists:
#     print(a.get_text())
# print(len(artists))


#print(titles)



#lxml
# 스크래핑하기 위해, lxml은 구문을 분석하기 위한 parser
#soup = BeautifulSoup(requests.text,'lxml')


#items = soup.find_all("li", attrs={"class": "search-product"})