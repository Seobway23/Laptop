import sys
sys.stdin= open('input.txt', 'r')

def dfs(i, sm):
    global ans
    if i == N:
        if sm >= K:
            ans = min(ans, sm-K)
        return
    # 선택O
    dfs(i + 1, sm + lst[i])

    # 선택 X
    dfs(i + 1, sm)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 10000 * len(lst)
    dfs(0, 0)
    print(f"#{test_case} {ans}")