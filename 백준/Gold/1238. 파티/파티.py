
import heapq


def dijkstra(start, graph, N):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue

        for next_node, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(q, (distance, next_node))

    return distances


n, m, x = map(int, input().split())
roads = [ list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]

for s, e, t in roads:
    graph[s].append([e, t])

# X -> 마을까지 최단 거리
shortest_to_X = dijkstra(x, graph, n)

max_time = 0
for i in range(1, n + 1):
    if i != x:
        # 최단 시간 계산
        shortest_from_X = dijkstra(i, graph, n)
        # 합친 시간 계산
        round_trip_time = shortest_to_X[i] + shortest_from_X[x]
        max_time = max(max_time, round_trip_time)

print(max_time)