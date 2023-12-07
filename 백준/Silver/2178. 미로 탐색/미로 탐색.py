
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

start = [0, 0]
q = deque()
q.append(start)

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]   # 우 하 좌 상
ans = 1
visit = []


def is_in_range(i, j):
    return 0 <= i < n and 0 <= j < m


def bfs():
    global ans
    while q:
        ti, tj = q.popleft()

        for k in range(4):  # 우 하 상 좌
            ni, nj = ti + di[k], tj + dj[k]
            # print(ni, nj)
            # 범위내 and
            if is_in_range(ni, nj) and arr[ni][nj] == 1:
                if visited[ni][nj] == 0:
                    visit.append([ni, nj])
                    q.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1

    return visited[n-1][m-1] + 1    # 시작 위치 포함


print(bfs())