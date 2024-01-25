n = int(input())
lst = [0] * (n + 1)     # 계단 점수 리스트 크기: n + 1
for i in range(1, n + 1):
    lst[i] = int(input())

dp = [0] * (n + 1)      # dp 리스트 크기: n + 1
dp[1] = lst[1]

#1일 경우도 고려해야 하기 때문에 if 문 추가
if n > 1:
    dp[2] = lst[1] + lst[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(dp[n])