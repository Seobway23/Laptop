import math

arr = []
N = int(input())
ans= [math.inf for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for tX in range(N):
    for tY in range(N):
        cnt_X, cnt_Y = arr[tX][0], arr[tY][1]

        distance = []
        for idx in range(N):
            distance.append(abs(cnt_X-arr[idx][0]) + abs(cnt_Y-arr[idx][1]))

        distance.sort()
        sm = 0
        for index in range(N):
            sm += distance[index]
            ans[index] = min(ans[index], sm)


print(*ans)