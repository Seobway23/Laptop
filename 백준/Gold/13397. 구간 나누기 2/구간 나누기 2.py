n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 최대 최소의 차이, 가장 큰 수, start  = 0
start, end = 0, 10001
ans = 0

def divide_segs(limit):
    # 0번 째부터 min,max 체크하니까, segs는 1번부터임
    segs = 1
    cur_min =  cur_max = arr[0]

    for i in arr[1:]:
        # 하나씩 순회 하면선 min, max 갱신
        if cur_min > i: cur_min = i
        if cur_max < i: cur_max = i

        # 최솟값 확인
        if cur_max - cur_min > limit:
            segs += 1

            # 세그멘트 하나 더 나오는 거니까 초기화 시켜야 함
            cur_min = cur_max = i

            if segs > m:
                # m 보다 커야 하니까, m 이상의 수 아무거나
                return 10001

    return segs

# 최솟값 갱신
while start <= end:
    mid = (start + end) // 2

    if divide_segs(mid) <= m:
        # ans 갱신 -> m 안쪽 -> 후보값 포함됨
        ans = mid
        end = mid - 1

    else:
        start = mid + 1


print(ans)