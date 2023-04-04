import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
'''
출발 왼쪽 위 , 도착 오른쪽 아래, N이 100이라 절대 dfs 불가
'''


def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.popleft()
        # 4 방향, 미방문
        for di, dj in ((-1, 0),(0, 1),(1, 0),(0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj] - arr[ci][cj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj] - arr[ci][cj] + 1

    return v[ei][ej]


T = int(input())
for test_case in range(1, T+1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[10000]*N for _ in range(N)]
    ans = bfs(0, 0, N-1, N-1)
    print(v)
    print(f"#{test_case} {ans}")

