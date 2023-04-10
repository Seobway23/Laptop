import sys
sys.stdin = open('input.txt', 'r')

def RED(i,j):
    if dp[i][j]:
        return dp[i][j]

    result = 13*N
    for di, dj in (0, 1), (1, 0):
        d = result
        ddd = arr[i][j]
        aaa = dp
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            result = min(result, arr[i][j] + RED(ni, nj))
    dp[i][j] = result
    return result


T = int( input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #반복연산 줄이는 DP
    dp = [[0]*N for _ in range(N)]
    # 기저 조건
    # 기저 조건으로부터 min 값을 계산해나가기
    dp[N-1][N-1] = arr[N-1][N-1]
    print(f'#{test_case} {RED(0,0)}')