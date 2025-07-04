from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
ans = 0
pic_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            q.append((i, j))
            cnt = 1
            pic_cnt += 1

            while q:
                ti, tj = q.popleft()
                # 4방향 탐색
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = ti + di, tj + dj

                    # 범위내 + 미방문
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        cnt += 1
            ans = max(ans, cnt)

print(pic_cnt)
print(ans)