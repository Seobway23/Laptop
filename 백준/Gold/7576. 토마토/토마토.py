from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[0] * m for _ in range(n)]

start_to = deque()
# start_to 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            start_to.append([i, j])
            visited[i][j] = 1

# 익은거 BFS 돌리기
info = -1
while start_to:
    info += 1
    for _ in range(len(start_to)):
        ti, tj = start_to.popleft()

        # 4 방향 탐색,
        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]

            # 범위내, 미방문 일 때
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                start_to.append([ni, nj])
                visited[ni][nj] = 1
                arr[ni][nj] = 1

# 정답 확인
ans, cnt = -1, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            cnt += 1
if cnt == m*n:
    ans = info

print(ans)
