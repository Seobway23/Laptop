
from collections import deque

# dfs
def dfs(si, sj, depth, lst, v):
    new_arr = [row[:] for row in arr]
    # 종료 조건
    if depth > 3:
        return

    if len(lst) == 3:
        all_lst.append(lst[:])
        return

    for i in range(si, n):
        for j in range( m):
            if not arr[i][j] and not v[i][j]:
                # v, lst 추가
                v[i][j] = 1
                lst.append((i, j))
                dfs(i, j, depth + 1, lst, v)
                # v, lst 제거
                lst.pop()
                v[i][j] = 0

# bfs
def bfs(new_arr):
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                while q:
                    ti, tj = q.popleft()

                    # 4방향 탐색
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ti + di, tj + dj

                        # 미방문, 0일 때, 2 추가
                        if 0 <= ni < n and 0 <= nj < m and not new_arr[ni][nj]:
                            new_arr[ni][nj] = 2
                            q.append((ni, nj))
                            v[ni][nj] = 1
    return new_arr

# input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# init
v = [[0] * m for _ in range(n)]
ans = 0
all_lst = []

# 3개 선정
for i in range(n):
    for j in range(m):
        if not arr[i][j] and not v[i][j]:
            v[i][j] =1
            # dfs 플래그는 탈출을 위해 n + 1 turn 을 무조건 해야 함
            dfs(i, j, 1, [(i, j)], v)
            v[i][j] = 0

# 가장 최적 찾기
for lst in all_lst:
    new_arr = [row[:] for row in arr]

    # 벽 3개 세우기
    for i, j in lst:
        new_arr[i][j] = 1

    # 바이러스 전파
    new_arr = bfs(new_arr)
    cnt = sum(1 for row in new_arr for cell in row if cell == 0)

    # answer 갱신
    ans = max(ans, cnt)

print(ans)
