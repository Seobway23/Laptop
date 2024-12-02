# init
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir_lst =[list(map(int, input().split())) for _ in range(M)]
# [0]: 원점, [1]: ←, [2]: ↖, [3]: ↑, [4]: ↗, [5]: →, [6]: ↘, [7]: ↓, [8]: ↙
dir = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

# 방향은 ->  % n  으로 유지
cloud_lst = ((N-1, 0), (N -1, 1), (N-2, 0), (N-2, 1))

# d : 움직일 칸수, s : dir 방향
for d, s in dir_lst:
    v = [[0] * N for _ in range(N)]
    cur_cloud = []

    #  raining  += 1
    for ci, cj in cloud_lst:
        ni, nj = (ci + dir[d][0] * s) % N, (cj + dir[d][1] * s) % N
        arr[ni][nj] += 1    # 비 내리기, + 1
        v[ni][nj] = 1       # 방문 표시
        cur_cloud.append((ni, nj))

    # copy water
    for ci, cj in cur_cloud:
        for di, dj in ((1, 1), (-1, -1), (1, -1), (-1, 1)): # 대각선
            # move가 아니기 때문에 % N 로 하면 안됨
            ni, nj = (ci + di), (cj + dj)

            # 범위내, 미방문, 0보다 클 때
            if 0 <= ni < N and 0 <= nj < N  and arr[ni][nj] > 0:
                arr[ci][cj] += 1

    # 새로운 구름 생성 및 물의 양 감소
    new_cloud_lst = []
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] >= 2:
                arr[i][j] -= 2
                new_cloud_lst.append((i, j))
    cloud_lst = new_cloud_lst  # 다음 이동을 위해 구름 리스트 업데이트

# 물의 양 합
print(sum( map(sum, arr) ))