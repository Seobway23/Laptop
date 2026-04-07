n = int(input())
arr = list(map(int, input().split()))

prefix = 0
ans = 0
for i in range(n):
    prefix += arr[i]
    ans += abs(prefix)

print(ans)
