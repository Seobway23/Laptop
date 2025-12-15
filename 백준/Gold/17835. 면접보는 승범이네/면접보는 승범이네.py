import heapq

N, M, K = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, c = map(int, input().split())
    arr[v].append((u, c))

starts = list(map(int, input().split()))

# pq
pq = []
INF = 10 ** 18
dist = [INF] * (N + 1)
# 0 초기화
dist[0] = -1

for s in starts:
    # 가지 치기를 위한 초기화
    dist[s] = 0
    heapq.heappush(pq, (0, s))


while pq:
    d, u = heapq.heappop(pq)

    # 가지 치기
    if d != dist[u]:
        continue

    for i in arr[u]:
        v, w = i[0], i[1]

        nd = d + w

        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))



ans, idx = 0, 0
for i in range(N + 1):
    if ans < dist[i]:
        ans = dist[i]
        idx = i

print(idx)
print(ans)







