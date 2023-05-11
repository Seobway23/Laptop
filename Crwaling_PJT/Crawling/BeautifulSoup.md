# 목표
'''
대목표 : 코스피 200 순위 중 가격이 10% 이상 변동되는 Stock의 이슈 파악
구현 목표: 
1. 크롤링 활용한 코스피 200 순위, 이슈 파악 크롤링
2. 게시판으로 보여주기
3. 장이 끝나는 3시에 코스피 200 순위 파악 
4. 매주 4시 업데이트
- 업데이트할 때, 
'''

# 계획
'''
1. bs4 -> csv or json file save(done)
2. selenium -> Using XPath, automotive click(done)
3. json file -> To link Json and django page
4. django 환경 익숙해지기
5. vue.js 이용하여 fron 환경 만들기
'''

# 절차
1. webdriver사용을 위해 chrome driver를 깔아야 함
- chrome 버전과 맞는 chrome driver를 깔아야 함



참고자료
=======
md 자료
https://www.youtube.com/watch?v=eHUVvQ2AHh0


- 공홈
>https://www.crummy.com/software/BeautifulSoup/bs4/doc/

- select
https://parkjh7764.tistory.com/139?category=1314478

- stackoverflow
https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json

11_bs4.py
- csv, json 저장

13_data_to_json.py
- json 바로 저장
- 들어오는 데이터 -> 딕셔너리화해서 바로 json형태로 저장


### select
1. 태그 이름만 특정
- soup.select_one('p')
2. 태그 class 특정
- soup.select_one('.youngone')
3. 태그 이름과 class 모두 특정
- soup.select_one('p.youngone')
4. 태그 id 특정
- soup.select_one('#junu')
5. 태그 이름과 id 모두 특정
- soup.select_one('p#junu')
6. 태그 이름과 class, id 모두 특정
- soup.select_one('p.youngone#junu')


### find
find
soup.find('div').find('p')
select
soup.select_one('div > p')