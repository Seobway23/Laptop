import heapq

V, E = map(int, input().split())
s = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10 ** 18
dist = [INF] * (V + 1)
dist[s] = 0

pq = [(0, s)]

while pq:
    # d: 거리, u: 시작, v: 끝
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in graph[u]:
        # nd : 다음 거리
        nd = d + w
        # 가중치 갱신
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

for i in range(1, V + 1):
    print("INF" if dist[i] == INF else dist[i])
