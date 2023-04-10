import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, cur):
    global ans
    #종료 조건
    if n == N:
        if v[A] < v[B]:
            ans = min(ans, sm + arr[cur][1])
        return

    for i in range(N):
        if v[i] == 0 and i != n:
            v[i] = n
            sm += arr[n][i]
            dfs(n + 1, sm, i)
            v[i] = 0
            sm -= arr[n][i]



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    v = [0]*(N +1)
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())
    ans = 100 * N+1
    dfs(1, 0, 0)
    print(f"#{test_case} {ans}")