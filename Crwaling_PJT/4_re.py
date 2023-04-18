# 정규식 

import re
p = re.compile("ca.e") # . : 하나의 문자
# . (ca.e): 하나의 문자를의미 > care, cafe, case | caffe(X)
# ^ (^de) : 문자열의 시작 > dest, destination (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base (O) | face(X)

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("care") #주어진 문자열의 처음부터 일치하는 지 확인
print(m.group())

m = p.search("good care")
print_match(m)

# 1. p = re.compile("원하는 형태")
# 2. m = 