import sys
sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
Mlst = [0] + list(map(int,input().split()))
Clst = [0] + list(map(int, input().split()))
c_max = sum(Clst)
result = c_max

dp = [[-1]*(c_max+1) for _ in range(N)]

for i in range(1, N+1):

    for j in range(1, c_max+1):
        # i는 cost, j -> m 최댓값 갱신
        if j < Clst[i]:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(Mlst[i] + dp[i-1][j-Clst[i]], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)

print(result) if M != 0 else print(0)

