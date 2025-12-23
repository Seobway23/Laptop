import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(M):
        data = list(map(int, input().split()))
        k = data[0]
        singers = data[1:]
        for i in range(k - 1):
            a = singers[i]
            b = singers[i + 1]
            graph[a].append(b)
            indegree[b] += 1

    q = deque(i for i in range(1, N + 1) if indegree[i] == 0)
    res = []

    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if len(res) != N:
        print(0)
    else:
        sys.stdout.write("\n".join(map(str, res)))

if __name__ == "__main__":
    solve()
