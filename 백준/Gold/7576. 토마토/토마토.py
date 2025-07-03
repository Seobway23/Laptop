from collections import deque

# m: col, n: row
m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1을 먼저 찾기
start = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            start.append((i, j))


q = deque(start)
cnt = 0

while q:
    flag = 0
    for _ in range(len(q)):
        ti, tj = q.popleft()

        # 4방향 탐색
        for di, dj  in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            ni, nj = ti + di, tj + dj

            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = 1
                flag = 1

    if flag == 1:
        cnt += 1


zero = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero = 1
            break

if zero == 1:
    print(-1)

else:
    print(cnt)


