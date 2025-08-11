import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 시작 시간 기준 Sort
arr.sort( key = lambda x : x[0])

# 순회 -> 우선 순위 => 이미 시작 시준 기준 정렬을 했기 때문에, 끝나는 시간의 우선순위를 arr를 순회를 통해 찾을 수 있음
hq = []
for start, end in arr:
    # 만약 hq가 없다면 push
    if not hq:
        heapq.heappush(hq, end)

    # hq가 있을 때
    else:
        # 지금 강의중 end 가  현재 start 보다  클 경우
        if hq[0] > start:
            # 강의실 추가
            heapq.heappush(hq, end)

        # 강의중 end 가 현재 start 와 같거나 큰 경우
        else:
            # 강의중 pop, 현재 강의 end push
            heapq.heappop(hq)
            heapq.heappush(hq, end)

print(len(hq))