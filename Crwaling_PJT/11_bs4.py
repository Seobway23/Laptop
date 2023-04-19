import csv, json
from bs4 import BeautifulSoup
import requests
import pandas

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

# csv 파일 저장
filename = f"{keyword}.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = ["순번", "이름", "제목", "내용"]
writer.writerow(title)

#빈 칸은 .으로 바꾸면 됨
# class의 경우 .{class_name} 으로 접근하면 됨
items = soup.select(".news_tit")
contents = soup.select(".api_txt_lines.dsc_txt_wrap")

# row 가져와서 하나씩 저장
for i in range(len(items)):
    item = items[i].text
    content = contents[i].text
    writer.writerow([i+1, name, item, content])
f.close()


# 1번째 방법
csvfile = open(filename, 'r', encoding="utf-8-sig" )
jsonfile = open(f'{keyword}.json', 'w', encoding="utf-8-sig")

filednames = title
reader = csv.DictReader(csvfile, filednames)
rows = []
for row in reader:
    rows.append(row)
json_row = json.dump(rows, jsonfile, ensure_ascii=False, indent=4)

csvfile.close()
jsonfile.close()


# 2번째 방법
# csvfile = open(filename, 'r', encoding="utf-8-sig" )
# jsonfile = open(f'{keyword}.json', 'w', encoding="utf-8-sig")

# filednames = title
# reader = csv.DictReader(csvfile, filednames)
# jsonfile.write('[')
# for row in reader:
#     json.dump(row, jsonfile, ensure_ascii=False)
#     jsonfile.write(',\n')

# jsonfile.write('[')
# #ensure_ascii -> 






# 시행 착오
'''
# csv -> json 저장 #잘못 되었음 
df = pandas.read_csv(filename)
json_data = df.to_json(orient='records')

with open(filename.json, 'w') as file:
    file.write(json_data)

# 파일 이름에 띄어쓰기가 있으면 안됨.
with open("삼성전자 주식.json", 'w') as file:
    file.write(json_data)

'''


