import heapq

# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

hq = []
for i in arr:
    heapq.heappush(hq, i)

while m:
    t1 = heapq.heappop(hq)
    t2 = heapq.heappop(hq)

    # 합치기
    sm = t1 + t2

    # 우선 순위 큐에 추가
    for _ in range(2):
        heapq.heappush(hq, sm)
    m -= 1

print(sum(hq))