# input
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [(m1 * 100 + d1, m2  * 100 + d2) for m1, d1, m2, d2 in arr]

# sort
arr.sort()  # 첫번째, start 를 기준 으로 정렬

# init value
cur, goal = 301, 1201   # [start, end) 이다, 따라서 1130 + 1 => 1201 을 goal 로 잡는다
i = 0   # while 돌릴 i index 변수
ans = 0 # ans -> 출력 값

while cur < goal:
    max_end = cur
    # max_end 갱신
    while i < n and arr[i][0] <= cur:   # start 가 cur 보다 작으면
        max_end = max(arr[i][1], max_end)   # max_end 갱신
        i += 1  # i 갱신 => index ++


    # 갱신 실패
    if max_end == cur:
        print(0)
        exit()

    cur = max_end
    ans += 1

print(ans)



