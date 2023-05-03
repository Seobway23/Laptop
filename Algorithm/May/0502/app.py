import sys
sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
Mlst = [0] + list(map(int, input().split())) # 메모리
Clst = [0] + list(map(int, input().split())) # 비용
c_max = sum(Clst)
dp = [[0]*(c_max + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, sum(Clst) + 1):
        # i는 cost, j -> m 최댓값 갱신
        if j < Clst[i]:
            dp[i][j] = dp[i - 1][j]
        else: # 이전 비용을 이용한 현재 비용 DP 테이블 점화식
            dp[i][j] = max(Mlst[i] + dp[i - 1][j - Clst[i]], dp[i - 1][j])

        if dp[i][j] >= M:
            c_max = min(c_max, j)
if M != 0:
    print(c_max)
else:
    print(0)