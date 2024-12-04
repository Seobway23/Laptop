from collections import deque
from itertools import combinations

# bfs 함수는 기존과 동일
def bfs():
    new_arr = [row[:] for row in arr]
    q = deque()
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                q.append((i, j))

    while q:
        ti, tj = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if new_arr[ni][nj] == 0:
                    new_arr[ni][nj] = 2
                    q.append((ni, nj))
    cnt = sum(row.count(0) for row in new_arr)
    return cnt

# input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# init
empty_positions = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 0]
ans = 0

# 3 walls combi
for walls in combinations(empty_positions, 3):
    # 벽 설치
    for i, j in walls:
        arr[i][j] = 1

    # 바이러스 전파
    safe_area = bfs()
    ans = max(ans, safe_area)

    # 벽 제거
    for i, j in walls:
        arr[i][j] = 0

print(ans)
