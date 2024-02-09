from collections import deque

m, n, h = map(int, input().split())
arr = list(list(list(map(int, input().split())) for _ in range(n)) for _ in range(h))
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

di = [0, 0, -1, 1, 0, 0]
dj = [-1, 1, 0, 0, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])
                visited[i][j][k] = True

            if arr[i][j][k] == -1:
                visited[i][j][k] = True

cnt = -1
while q:
    cnt += 1
    for _ in range(len(q)):
        ti, tj, tk = q.popleft()

        for d in range(6):
            ni = ti + di[d]
            nj = tj + dj[d]
            nk = tk + dk[d]

            # 범위내
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
                # print("arr:", arr[ni][nj][nk], "visited:", visited[ni][nj][nk])
                if arr[ni][nj][nk] == 0 and visited[ni][nj][nk] == False:
                    q.append([ni, nj, nk])
                    visited[ni][nj][nk] = True


sm = 0
for i in visited:
    for j in i:
        sm += sum(j)

if sm == m * n * h:
    print(cnt)

else:
    print(-1)