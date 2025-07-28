from collections import deque

# 1. 입력
m, n = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = 0  # 처음은 0 이므로 0, 0 갱신
di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]

# 2. q 추가
q = deque()
q.append((0, 0))

# 3. bfs, 최소값 갱신
while q:
    ci, cj = q.popleft()
    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            # cost = 현재 dist 거리 + next 위치( 벽이면 + 1)
            cost = dist[ci][cj] + arr[ni][nj]

            # 최소값 갱신
            if dist[ni][nj] > cost:
                dist[ni][nj] = cost

                if arr[ni][nj] == 1:
                    q.append((ni, nj)) # 1이라면 마지막 추가

                else:
                    q.appendleft((ni, nj)) # 0은 우선 추가

print(dist[n-1][m-1])