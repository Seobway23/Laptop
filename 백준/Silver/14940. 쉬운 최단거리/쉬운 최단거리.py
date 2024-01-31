from collections import deque

# 입력
N, M = map(int, input().split())
board = []
queue = deque([])
visit = [[False]*M for _ in range(N)]
res = [[-1]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        # 목표지점 찾기
        if row[j] == 2:
            queue.append((i, j))
            visit[i][j] = True
            res[i][j] = 0

        # 벽 기록
        if row[j] == 0:
            res[i][j] = 0
    board.append(row)

# BFS 탐색
di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx, ny = x + di[k], y + dj[k]

        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 1:
            queue.append((nx, ny))
            visit[nx][ny] = True
            res[nx][ny] = res[x][y] + 1

# 출력
for i in range(len(res)):
    print(*res[i])