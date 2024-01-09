n = int(input())
lst = []
dic = dict()
for _ in range(n):
    s = int(input())
    lst.append(s)
    dic[s] = 0

# 1 산술 평균
first = round(sum(lst) / n)
print(first)

# 2 중앙값
avg = sorted(lst)
if n % 2 == 1:
    print(avg[n//2])

else:
    i = avg[n//2 - 1] + avg[n//2]
    j = round(i // 2)
    print(j)

# 3 최빈값
for i in lst:
    dic[i] += 1

key_value_lst = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
if len(key_value_lst) > 1 and key_value_lst[0][1] == key_value_lst[1][1]:
    print(key_value_lst[1][0])

else:
    print(key_value_lst[0][0])

# 4 최대 최소 차이
print(avg[-1] - avg[0])
