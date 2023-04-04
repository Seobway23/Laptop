import sys
sys.stdin = open('input.txt', 'r')

'''
12원소 집합 A, N개의 원소, K의 원소합의 갯수 출력
'''

def dfs(n,index, sm):
    global ans
    #종료 조건
    if index == 12: #index 12까지 이므로 13일 때 X를 선택했을 때를 종료 조건으로 잡음
        if n == N:
            if sm == K:
                ans += 1
        return

    # 하부 호출
    dfs(n, index+1, sm)
    dfs(n+1, index+1, sm + A[index])


A = list(i for i in range(1, 12 + 1))

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")