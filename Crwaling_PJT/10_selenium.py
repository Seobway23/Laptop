from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager())
# crawling_url = "http:naver.com"
# driver.get(crawling_url)

# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("http:naver.com")

browser = webdriver.Chrome()
browser.get("http://naver.com")
#112.0.5615.121(공식 빌드) (32비트)