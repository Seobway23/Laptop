n = input().split('-')

num = []

for i in n:
    sm = 0
    temp_nums = i.split("+")
    for j in temp_nums:
        sm += int(j)
    num.append(sm)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)