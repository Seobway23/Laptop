t = int(input())
lst = list(list(map(int, input().split())) for _ in range(t))
lst.sort(key=lambda x: (x[1], x[0]))

# 0번째 로직
cnt = 1
e = lst[0][1]

# 1부터 로직
for i in range(1, t):
    if lst[i][0] >= e:
        cnt += 1
        e = lst[i][1]

print(cnt)