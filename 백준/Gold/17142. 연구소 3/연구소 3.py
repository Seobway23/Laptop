from collections import deque
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

two_lst = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 2]

def BFS(active):
    # v: -1=벽, -2=미방문, 그 외=도달 시간
    v = [[-2]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                v[i][j] = -1

    # 활성 바이러스를 다중 시작점(시간 0)으로
    for i, j in active:
        v[i][j] = 0
        q.append((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 벽이 아닐 때
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == -2 and arr[ni][nj] != 1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


    # 빈 칸만 판별
    mx = 0
    for i in range(n):
        for j in range(n):
            # 빈 칸 이면서
            if arr[i][j] == 0:
                # 미방문 이면 return
                if v[i][j] == -2:
                    return -1
                mx = max(mx, v[i][j])
    return mx

for active in combinations(two_lst, m):
    t = BFS(active)
    if t != -1:
        ans = min(ans, t)

print(-1 if ans == float('inf') else ans)