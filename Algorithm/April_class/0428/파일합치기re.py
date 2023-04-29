import sys, math
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    # 누적합 sm
    sm = [0]*N
    for i in range(N):
        sm[i] = sum(lst[:i+1])
    # DP 누적 최소 테이블, DP[i][j] -> i부터 j까지 합
    DP = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 최솟값 찾기 위한 반복
            small = math.inf
            for k in range(j-i+1):
                ign = DP[i][k] + DP[i+k][j] + sm[j] - sm[i]
                DP[i][j] = min(small, ign)

    print(DP[0][N-1])
