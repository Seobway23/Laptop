n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0
for i in range(1, n + 1):
    for ci in range(i):
        ans += lst[ci]

print(ans)
