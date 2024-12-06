h, w, n, m = map(int, input().split())
ans = 0
for i in range(0, h, n + 1):
    for j in range(0, w, m + 1):
        ans += 1

print(ans)