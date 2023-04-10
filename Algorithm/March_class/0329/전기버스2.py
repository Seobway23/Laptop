import sys
sys.stdin =open('input.txt', 'r')

def dfs(n, cnt, sm):
    global ans
    # 가지치기 : 지정 최솟값보다 커지는 경우
    if ans <= cnt:
        return

    # N일 때, 원하는 값 중 min 값 return
    if n == N:
        ans = min(ans, cnt)
        return

    # 교체하지 않는 경우: 잔량>0 일때만 가능
    if sm > 0:
        dfs(n+1, cnt, sm -1)

    # 교체하는 경우: 항상 가능
    dfs(n+1, cnt + 1, lst[n] - 1)


T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N

    dfs(2, 0, lst[1] - 1)
    print(f"#{test_case} {ans}")