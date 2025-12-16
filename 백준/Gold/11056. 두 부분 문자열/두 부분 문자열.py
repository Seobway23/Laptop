A = input()
B = input()
N, M = len(A), len(B)

dp = [[0] * (M + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 이전게 같다면 하나 추가
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        # 다르다면 max 갱신
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

K = dp[N][M]
ans = N + M - K
print(ans)

