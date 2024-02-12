from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
di, dj = [1, -1, 0, 0], [0, 0, -1, 1]
first_ans, second_ans = 0, 0
q = deque()


def bfs(i, j):
    visited[i][j] = True
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))


# 그 전 구간
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            first_ans += 1

# G -> R 바꾸기
for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            second_ans += 1

print(first_ans, second_ans)
