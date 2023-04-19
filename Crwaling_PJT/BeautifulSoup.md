참고자료
=======
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