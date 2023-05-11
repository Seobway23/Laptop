
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

keyword= input("검색어를 입력하세요 : ")

search_url = base_url + keyword

search_url = "https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8"

browser = webdriver.Chrome()
#browser.get(search_url)

iframe = browser.find_elements(By.TAG_NAME, "iframe")
browser.switch_to.frame(iframe)
browser.switch_to.default_content()


# 서버 겟 요청보내면 응답 받음 d
r = requests.get(search_url)

#html 넣고, parser 분석
soup = BeautifulSoup(r.text, "html.parser")

#빈 칸은 .으로 바꾸면 됨
items = soup.select("main-shortcut-item")
print(items)
#soup 접근 방식 -> select, find 가능, select_one 한개 찾을 때

dess = soup.select("wrap-new api_animation")
print(dess)