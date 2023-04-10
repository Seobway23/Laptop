import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


'''
최소 연산, visited -> 100만개 , BFS
'''

def bfs(N, M):
    q = deque()
    q.append(N)
    v[N] = 1

    while q:
        # 먼저 간 곳을 cnt 하므로, 갱신할 필요가 없음, 빠른 곳 먼저 선정 -> 최선의 선택

        # 종료 조건을 while 문 안에다 넣음
        t = q.popleft()

        if t == M:
            return v[M] - 1

        # 네 방향, 범위 내, 미방문, 조건 맞으면 큐 삽입
        for i in (t-1, t + 1, t * 2, t - 10):
            if 1 <= i <= 1000000:
                if v[i] == 0:
                    v[i] = v[t] + 1
                    q.append(i)



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    v = [0] * (1000000 + 1)
    ans = bfs(N,M)
    print(f"#{test_case} {ans}")
