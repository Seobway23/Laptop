import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, n1, n2, n3, n4):
    global mn, mx
    # 종료 조건
    if n == N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return
    # [1] + 일 때
    if n1 > 0: dfs(n+1, sm+lst[n], n1-1, n2, n3, n4)
    # [2] - 일 때
    if n2 > 0: dfs(n+1, sm-lst[n], n1, n2-1, n3, n4)
    # [3] * 일 때
    if n3 > 0: dfs(n+1, sm*lst[n], n1, n2, n3-1, n4)
    # [4] * 일 때
    if n4 > 0: dfs(n+1, int(sm/lst[n]), n1, n2, n3, n4-1)



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    #연산자
    n1, n2, n3, n4 = map(int, input().split())
    lst = list(map(int, input().split()))
    mn = int(1e8)
    mx = int(-1e8)
    dfs(1, lst[0], n1, n2, n3, n4)
    print(f"#{test_case} {mx-mn}")