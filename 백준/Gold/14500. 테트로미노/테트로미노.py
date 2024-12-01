N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[0] * M for _ in range(N)]
ans = 0
mx = max(map(max, arr))

def dfs(lst, n, sm):
    global ans
    # 가지 치기
    if sm + (4 - n) * mx <= ans:
        return

    # 종료 조건
    if n == 4:
        ans = max(ans, sm)
        return

    # target
    for ci, cj in lst:
        for di, dj in dir:
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, lst 없을 때
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]==0:
                visited[ni][nj] = 1
                dfs(lst + [(ni, nj)], n + 1, sm + arr[ni][nj])
                visited[ni][nj] = 0

# 순회
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs([(i, j)], 1, arr[i][j])

print(ans)