from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 필요 자료 구조
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
visited = [[False] * m for _ in range(n)]

# 시작 위치 찾기
si, sj = -1, -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            si, sj = i, j

q = deque()
q.append((si, sj))
visited[si][sj] = True

# 탐색 시작
while q:
    ti, tj = q.popleft()
    for k in range(4):
        ni, nj = ti + di[k], tj + dj[k]
        # pprint(visited)
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] != "X":

            if arr[ni][nj] == "P":
                cnt += 1

            visited[ni][nj] = True
            q.append((ni, nj))

# 출력
if not cnt:
    print("TT")

else:
    print(cnt)