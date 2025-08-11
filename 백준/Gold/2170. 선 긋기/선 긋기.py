# input
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# init
arr.sort()
start, end = arr[0]
ans = 0
i = 1

while True:
    # end 갱신
    while i < n and end > arr[i][0]:     # i 범위내, next_start 가 end 보다 작으면
        end = max(end, arr[i][1])
        i += 1

    # ans 갱신
    ans += end - start

    # 만약 범위 밖이면 return
    if n <= i:
        break

    # start, end 갱신
    start, end = arr[i]

# output
print(ans)

