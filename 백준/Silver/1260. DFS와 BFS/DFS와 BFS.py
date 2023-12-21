from collections import deque


def dfs(start, visited):
    global dfs_ans
    visited[start] = 1
    dfs_ans.append(start)
    for i in nodes[start]:
        if i and not visited[i]:
            dfs(i, visited)
    return


def bfs(start):
    global bfs_ans
    visited = [0] * (n + 1) # 방문 표시
    q =deque()
    q.append(start)
    visited[start] = 1
    bfs_ans.append(start)

    while q:
        t = q.popleft()
        for i in nodes[t]:
            if i and not visited[i]:
                q.append(i)
                visited[i] = 1
                bfs_ans.append(i)
    return


# 입력
n, m, v = map(int, input().split())
nodes = [[] for _ in range(n + 1)]     # 0 인덱스 안씀

dfs_ans = []
bfs_ans = []

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for lst in nodes:
    if lst:
        lst.sort()

# dfs
visited = [0] * (n + 1)
dfs(v, visited)

# bfs
bfs(v)

print(*dfs_ans)
print(*bfs_ans)
