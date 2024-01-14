n = int(input())

lst = list(list(map(int, input().split())) for _ in range(n))

lst.sort(key=lambda x: (x[1], x[0]))

for i, j in lst:
    print(i, j)