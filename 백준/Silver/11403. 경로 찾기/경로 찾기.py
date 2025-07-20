from collections import deque


def bfs(si, end):
    q = deque()
    visited = [0] * n
    # 순회 & q 추가
    for j in range(n):
        if arr[si][j] == 1:
            if j == end: return 1   # end 처리
            q.append(j)
            visited[j] = 1
    # BFS
    while q:
        ci = q.popleft()

        for j in range(n):
            if arr[ci][j] == 1 and visited[j] == 0:
                if j == end: return 1   # end 처리
                q.append(j)
                visited[j] = 1
    return 0


n= int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans[i][j] = bfs(i, j)

for i in ans:
    print(*i)