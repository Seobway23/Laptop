n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

start, end = max(arr), sum(arr)

def divide_seg(limit):
    # 세그 1개부터 시작
    segs = 1
    sm = arr[0]

    for i in arr[1:]:
        if  sm + i > limit:
            segs += 1
            sm = i

        else:
            sm += i

    return segs

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    if divide_seg(mid) <= m:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)

