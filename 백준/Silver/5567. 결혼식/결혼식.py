from collections import deque

n = int(input())
m = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    arr[n1-1][n2-1] = arr[n2-1][n1-1] =  1

invite = set()
q = deque([(0, 0)])
visited = [[0] * n  for _ in range(3)] # v[i][j] -> 깊이 d에서 j를 처리 했는지
visited[0][0] = 1

while q:
    ci, depth = q.popleft()
    if depth == 2:
        continue

    for j in range(n):
        if arr[ci][j] == 1 and visited[depth + 1][j] == 0:
            visited[depth + 1][j] = 1
            if j != 0:
                invite.add(j)
            q.append((j, depth + 1))

print(len(invite))