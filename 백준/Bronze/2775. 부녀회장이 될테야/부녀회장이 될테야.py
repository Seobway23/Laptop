# k 가 작으므로 미리 DP 구하기
floor = 14 + 1
dp = list([0] * floor for _ in range(floor))    # 0은 거둘뿐

for i in range(floor):
    dp[0][i] = i
    dp[i][1] = 1

for i in range(1, floor):   # 행
    for j in range(1, floor):   # 열
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    print(dp[n][k])
