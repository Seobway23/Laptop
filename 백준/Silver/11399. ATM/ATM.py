n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
mul = n
for j in arr:
    ans += mul * j
    mul -= 1



print(ans)