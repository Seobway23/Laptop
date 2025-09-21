
import math

n, m, l = map(int, input().split())
ans = 0
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()
# print(arr)

gaps = [arr[i+ 1] - arr[i] for i in range(len(arr) - 1)]
# print(gaps)
# 시작, 끝 정하기
s, e = 1,  max(gaps)

def divide(limit):
    cnt = 0
    for g in gaps:
        # 현재 구한 cnt는 조각, 우리가 구해야 하는 거는 양쪽 노드 제외한 노드
        # 따라서 현재 조각 - 1 하면 된다.
        cnt += math.ceil(g / limit )- 1
    return cnt

# 이분 탐색
while s <= e:
    mid  = (s + e) // 2
    if divide(mid) <= m:
        pass
        ans = mid
        e = mid - 1

    else:
        s = mid + 1


print(ans)