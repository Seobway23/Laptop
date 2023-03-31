import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, n1, n2, n3, n4):
    global mn, mx
    if n == N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    #  해당 연산자카드가 존재하는 경우 하부 호출
    if n1 > 0:  # 더하기 연산자카드 있음
        dfs(n + 1, sm + lst[n], n1 - 1, n2, n3, n4)
    if n2 > 0:  # 빼기 연산자카드 있음
        dfs(n + 1, sm - lst[n], n1, n2 - 1, n3, n4)
    if n3 > 0:  # 곱하기 연산자카드 있음
        dfs(n + 1, sm * lst[n], n1, n2, n3 - 1, n4)
    if n4 > 0:  # 나누기 연산자카드 있음 => 주의! 파이썬의 // 연산자는 음수 연산시 생각과 다르게 동작할 수 있음 (나머지는 양수이므로..)
        dfs(n + 1, int(sm / lst[n]), n1, n2, n3, n4 - 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n1, n2, n3, n4 = map(int, input().split())
    lst = list(map(int, input().split()))
    mn = int(1e8)
    mx = int(-1e8)

    dfs(1, lst[0], n1, n2, n3, n4)
    print(f'#{test_case} {mx - mn}')