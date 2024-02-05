from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
di, dj = [0, 0, -1, 1], [1, -1, 0, 0]
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt = 1
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                for _ in range(len(q)):
                    ti, tj = q.popleft()

                    for k in range(4):
                        ni, nj = ti + di[k], tj + dj[k]

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1and not visited[ni][nj]:
                            q.append((ni, nj))
                            visited[ni][nj] = True
                            cnt += 1

            ans.append(cnt)

# 정답
ans.sort()
print(len(ans))
for i in ans:
    print(i)
