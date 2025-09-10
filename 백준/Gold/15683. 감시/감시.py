n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float("inf")

# 1~5 CCTV 방향 설정
cctv_dir = [[],
            [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]], # 1
            [[(1, 0), (-1, 0)], [(0, -1), (0, 1)], [(1, 0), (-1, 0)], [(0, -1), (0, 1)]], # 2
            [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]], # 3
            [[(-1, 0), (0, -1), (0, 1)], [(1, 0), (0, -1), (0, 1)], [(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)]], # 4
            [[(1, 0), (-1, 0), (0, -1), (0, 1)], [(1, 0), (-1, 0), (0, -1), (0, 1)], [(1, 0), (-1, 0), (0, -1), (0, 1)] ,[(1, 0), (-1, 0), (0, -1), (0, 1)]]  # 5
            ]


# cctv list 갱신
cctv_lst  = []
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv_lst.append((i, j, arr[i][j]))


def dfs(idx, rotate, arr):
    global ans
    # 4방향 탐색

    if idx == len(cctv_lst):
        # pprint(arr)
        cnt = 0
        for i in range(n):
            for j in  range(m):
                if arr[i][j] == 0:
                    cnt += 1
        ans = min(cnt, ans)
        return

    # BFS 돌리기
    new_arr = [row[:] for row in arr]


    ci, cj, cur_cctv = cctv_lst[idx]
    # 현재 cctv direction
    cur_cctv_dir = cctv_dir[cur_cctv]

    for di, dj in cur_cctv_dir[rotate]:
        k = 1
        while True:
            ni, nj = ci + di * k, cj + dj * k

            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 6:
                new_arr[ni][nj] = -1 # -1 은 확인한 거리
                k += 1
            else:
                 break

    # pprint(new_arr)
    # 다시 idx + 1 로 dfs 돌리기
    for rot in range(4):
        dfs(idx + 1, rot, new_arr)


for i in range(4):
    dfs(0, i, arr)


print(ans)