'''
html 안에 또 다른 html로 감싸졌기 때문에 안보였음 => iframe 때문
switch_to. 으로 접근해야 함

#112.0.5615.138(공식 빌드) (32비트)

iframe 크롤링 사용법
https://goodthings4me.tistory.com/162

selenium offical page
https://www.selenium.dev/documentation/webdriver/elements/finders/
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests

# driver = webdriver.Chrome(ChromeDriverManager())
# crawling_url = "http:naver.com"
# driver.get(crawling_url)

# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("http:naver.com")


# 1번과 2번은 같은 동작
# 1 while True:
#     pass

#==
# 2 options = Options()
# options.add_experimental_option('detach', True)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(options=options)

#얘는 동작을 다하면 꺼지기 때문에, 꺼지는 것이 당연함,
browser = webdriver.Chrome()
browser.get("http://naver.com")


# 바뀐 selsnium
elem = browser.find_element(By.CLASS_NAME,"link_login") 



# 태그 접근 방식
#find_element 요소에 접근
#send_keys -> 타이핑
'''
<input id="query" name="query" type="search" title="검색어 입력" maxlength="255" class="input_text" 
tabindex="1" accesskey="s" style="ime-mode:active;" autocomplete="off" placeholder="검색어를 입력해 주세요." 
onclick="document.getElementById('fbm').value=1;" value="" data-atcmp-element="">
'''
# browser.find_element(By.CLASS_NAME, "input_text").send_keys("name")
# browser.find_element(By.ID, "query").send_keys("name")
# browser.find_element(By.NAME, "query").send_keys("name")
# browser.find_element(By.CSS_SELECTOR, "[title:'검색어 입력']}").send_keys("name")

#XPath -> XML 문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어
elem = browser.find_element(By.XPATH,'//*[@id="query"]').send_keys("name")
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="search_btn"]/span[2]').click()

time.sleep(1)
browser.find_element(By.LINK_TEXT, "쇼핑LIVE").click()


name = "삼성전자"
search = f"{name} 주식"
browser.find_element(By.XPATH,'//*[@id="query"]').send_keys(search)
browser.find_element(By.XPATH,'//*[@id="search_btn"]/span[2]').click()
time.sleep(1)
newsXPath = '//*[@id="lnb"]/div[1]/div/ul/li[8]/a'
browser.find_element(By.XPATH,newsXPath).click()

html = '''
<a href="http://www.newsis.com/view/?id=NISX20230418_0002271456&amp;cID=13001&amp;pID=13000" 
class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*e.tit&amp;r=1&amp;i=88000127_000000000000000011810933&amp;g=003.0011810933&amp;u='+urlencode(this.href));" 
title="이재용 회장 취임 6개월…삼성 준법위, 지배구조 개편 '미온적'">이재용 회장 취임 6개월…<mark>삼성</mark> 준법위, 지배구조 개편 '미온적'</a>
'''

# bs string, text 차이점
# text는 그 안의 모든 글자를 다 가져옴
# string -> 빈칸, 빈줄이 있으면 못찾음


# 지금 bs4를 잘 못하고 있음 bs4 다시하기

#현재 browser 주소 
current_url = browser.current_url

soup  = BeautifulSoup(current_url, 'lxml')
logo = soup.select_one("a.news_tit")
print(logo.text)
print(logo.string)

#bs4 다시 보기