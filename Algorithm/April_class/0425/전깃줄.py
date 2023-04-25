import sys
sys.stdin= open('input.txt', 'r')

N = int(input())
v = [0]*501
ans = []
for _ in range(N):
    A, B = map(int, input().split())
    v[A] = B

for i in range(1, 501):
    if v[i] !=0:
        ans.append(v[i])

print(ans)

dp = [1 for i in range(len(ans))]
for j in range(len(ans)):
    for k in range(j):
        if ans[j] > ans[k]:
            dp[j] = max(dp[j], dp[k]+1)

print(len(ans) - max(dp))


