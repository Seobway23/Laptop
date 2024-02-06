import heapq

def max_heap(operations):
    heap = []
    result = []

    for op in operations:
        if op > 0:
            # 최대 힙 유지를 위한 음수 변환 추가
            heapq.heappush(heap, -op)

        else:
            # 비어있지 않으면 최대 값 결과 추가
            if heap:
                max_val = -heapq.heappop(heap)
                result.append(max_val)

            else:
                result.append(0)

    return result


n = int(input())
operations = [int(input()) for _ in range(n)]

for i in max_heap(operations):
    print(i)