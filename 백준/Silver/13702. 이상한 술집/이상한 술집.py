N, C = map(int, input().split())
clst = list(int(input()) for _ in range(N))

end = max(clst)
start = 1

while start <= end:
    mid = (start + end)//2
    # print(start, end, mid)
    cnt = 0
    for num in clst:
        cnt += num//mid
        rest = num%mid

    if cnt >= C:
        start = mid + 1

    else:
        end = mid - 1

print(end)