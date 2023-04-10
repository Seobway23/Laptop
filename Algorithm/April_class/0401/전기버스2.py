import sys
sys.stdin = open('input.txt', 'r')
'''
최소한의 교체횟수로 목적지에 도착해야 함
'''
def dfs(index, charge, sm):
    global ans
    if charge < 0:
        return
    if sm > ans:
        return

    #print('index:', index, 'charge:', charge, 'sm:', sm)
    # 종료 조건
    if index == N-1:
        if ans > sm and sm != 0:
            ans = sm
        return

    # 하부 호출
    # 충전 O
    dfs(index+1, lst[index]-1, sm + 1)
    # 충전 X
    dfs(index+1, charge-1, sm)


T = int(input())
for test_case in range(1, T+1):
    N, *lst = map(int, input().split())
    ans = 100000
    dfs(0, lst[0], 0)
    print(f"#{test_case} {ans}")
