
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited  = [ [0] * n for _ in range(n)]

# init
i, j = n // 2, n // 2 # 시작 위치
visited[i][j] = 1
dir = ((0, -1), (1, 0), (0, 1), (-1, 0)) # 좌, 하, 우, 상
spread = [(-1, -1, 10), (1, -1, 10), (0, -2, 5), (-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), (-1, 1, 1), (1, 1, 1), (0, -1, 55)]
size = 0    # 움직일 크기
k = 0       # 방향 인덱스
ans = 0     # 정답

# main loop
for t in range(n * 2):
    # size 크기 갱신
    if not t % 2:   size += 1

    # move
    for step in range(1, size + 1): # 1부터 size까지
        i, j = i + dir[k][0], j + dir[k][1]
        if 0 <= i < n and 0 <= j < n:  # 모래가 있다면
            visited[i][j] = 1

        #spread 처리
        if 0 <= i < n and 0 <= j < n and arr[i][j]: # 모래가 있다면
            cnt = 0
            for di, dj, percent in spread:
                ni, nj = i + di, j + dj

                # 마지막 a 일 때
                if percent == 55:
                    left_sand = arr[i][j] - cnt

                    # 범위 내라면
                    if 0 <= ni < n and 0 <= nj < n:  # 범위 내
                        arr[ni][nj] += left_sand
                    # 범위 밖이라면
                    else:
                        ans += left_sand


                else:
                    # sand 는 현재 위치의 sand 의 퍼센트
                    sand = arr[i][j] * percent // 100
                    if 0 <= ni < n and 0 <= nj < n: # 범위 내
                        arr[ni][nj] += sand
                        cnt += sand

                    else:
                        ans += sand
                        cnt += sand

            # arr[i][j] 0 처리
            arr[i][j] = 0
    # 방향 처리
    k = (k + 1 ) % 4
    for spr_num in range(len(spread)):
        # print(spread[spr_num], (-spread[spr_num][1], spread[spr_num][0], spread[spr_num][2]))
        spread[spr_num] = (-spread[spr_num][1], spread[spr_num][0], spread[spr_num][2])
        # tuple은 tuple로 바꾸기

print(ans)