import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N+1)]

stack = [(1, 0, False)]

while stack:
    u, parent, visited = stack.pop()

    if not visited:
        stack.append((u, parent, True))
        for v in graph[u]:
            if v != parent:
                stack.append((v, u, False))
    else:
        dp[u][1] = 1
        for v in graph[u]:
            if v == parent:
                continue
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])

print(min(dp[1][0], dp[1][1]))
