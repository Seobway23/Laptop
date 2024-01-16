from collections import deque


def find(nodes, s):
    num = [0] * (n + 1)
    visited = [s]
    q = deque()
    q.append(s)

    while q:
        t = q.popleft()
        for i in nodes[t]:
            if i not in visited:
                num[i] = num[t] + 1
                visited.append(i)
                q.append(i)
    return sum(num)


n, v = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(v):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)


result = []
for i in range(1, n + 1):
    result.append(find(nodes, i))

print(result.index(min(result)) + 1)

