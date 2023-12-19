from collections import deque


def dfs(graph, start, visited):
    global ans_dfs
    visited[start] = True
    ans_dfs.append(start)
    for node in sorted(graph[start]):
        if not visited[node]:
            dfs(graph, node, visited)
    return


def bfs(graph, start):
    global ans_bfs
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        ans_bfs.append(v)
        for node in sorted(graph[v]):
            if not visited[node]:
                queue.append(node)
                visited[node] = True
    return


# 예제 입력 1
n, m, v = map(int, input().split())
edges = [ list(map(int, input().split())) for _ in range(m)]

# 그래프 생성
graph = [[] for _ in range(n + 1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# DFS 와 BFS 수행
ans_dfs, ans_bfs = [], []
dfs(graph, v, [False] * (n + 1))
bfs(graph, v)

print(*ans_dfs)
print(*ans_bfs)