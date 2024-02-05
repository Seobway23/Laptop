def dfs(start, depth):
    # 노드 방문 체크 dfs
    visited[start] = True

    for j in graph[start]:
        if not visited[j]:
            dfs(j, depth + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
ans = 0

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            # 하나의 연결 요소 이기 때문에
            ans += 1
            visited[i] = 1

        else:
            # 방문 처리 + 1
            dfs(i, 0)
            ans += 1

print(ans)
