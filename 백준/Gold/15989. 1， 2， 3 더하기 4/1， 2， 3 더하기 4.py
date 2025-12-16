n = int(input())
arr = [int(input()) for _ in range(n)]
N = max(arr)
dp = [0] * (N + 1)
dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, N + 1):
        dp[i] += dp[i - num]

for t in arr:
    print(dp[t])

