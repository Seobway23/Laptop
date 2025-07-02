from collections import deque

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
# visited = [[0] * m for _ in range(m)]
dq = deque()
ans = []

for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    dif_y = y1 - y0
    dif_x = x1 - x0
    # 실제 값은 다 -1 해줘야 함

    for dy in range(dif_y):
        for dx in range(dif_x):
            nx, ny = x0 + dx, y0 + dy
            arr[ny][nx] = 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            # bfs 시작
            dq.append([i,j])
            arr[i][j] = 2 # 방문 표시

            cnt = 0
            while dq:
                ti, tj = dq.popleft()
                cnt += 1
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = ti + di, tj + dj

                    # 범위내, 미방문일 때
                    if 0<= ni < n and 0<= nj < m and arr[ni][nj] == 0:
                        dq.append([ni, nj])
                        arr[ni][nj] = 2

            ans.append(cnt)

print(len(ans))
print(*sorted(ans))



