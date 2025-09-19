n, m = map(int , input().split())
arr = [int(input()) for _ in range(n)]
ans = 0

s, e = max(arr), sum(arr)

def divide(limit):
    segs = 1
    s = 0
    for i in arr:
        if s + i > limit:
            s = i
            segs += 1
        else:
            s += i
    return  segs

while s <= e:
    mid = (s + e) // 2
    if divide(mid) <= m:
        # 갱신
        ans = mid
        e = mid  -1

    else:
        s = mid + 1


print(ans)