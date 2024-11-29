
import copy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
def move(arr, fishes):
    for i in range(1, 17): # 1~ 16까지
        # 없으면 다음 거
        if i not in fishes:
            continue

        ci, cj, dir = fishes[i]
        for k in range(8): # 0 ~ 7 까지
            n_dir = (dir + k) % 8
            # print("i: ", i, ", k: ", k, ", n_dir: ", n_dir)

            ni, nj = ci + directions[n_dir][0], cj + directions[n_dir][1]
            if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj] != 99:

                # 바꿔야 한다면
                if arr[ni][nj] > 0:
                    target = arr[ni][nj]
                    fishes[target] = ci, cj, fishes[target][2]

                # info update
                fishes[i] = (ni, nj, n_dir)
                arr[ni][nj], arr[ci][cj] = arr[ci][cj], arr[ni][nj]
                break # 이동 완료

    return arr, fishes


def dfs( arr, fishes, shk, shk_dir, cnt):
    global ans

    # 현재 상태 복사
    arr_copy = copy.deepcopy(arr)
    fishes_copy = fishes.copy()

    # 물고기 이동
    arr_copy, fishes_copy = move(arr_copy, fishes_copy)

    # 상어 위치 찾기
    possible_positions = []

    si, sj = shk
    for step in range(1, 4):
        ni, nj = shk[0] + directions[shk_dir][0] * step, shk[1] + directions[shk_dir][1] * step
        if 0 <= ni < 4 and 0 <= nj < 4:
            if arr_copy[ni][nj] > 0:
                possible_positions.append((ni, nj))
        else:
            break # 범위 밖이면 중지

    if not possible_positions:
        ans = max(ans, cnt)
        return

    # 모든 위치 재귀 호출
    for ni, nj in possible_positions:
        # 상태 복사
        new_arr = copy.deepcopy(arr_copy)
        new_fishes = fishes_copy.copy()

        # 물고기 먹기
        fish_num = new_arr[ni][nj]      # 물고기 번호
        fish_dir = new_fishes[fish_num][2]  # 상어가 먹은 물고기 방향

        # 상어 위치 갱신
        new_arr[si][sj] = 0         # 이전 상어 위치 0
        new_arr[ni][nj] = 99        # 다음 상어 위치 99
        del new_fishes[fish_num]    # 물고기 delete

        dfs(new_arr, new_fishes, (ni, nj), fish_dir, cnt + fish_num)


n = 4
fishes = dict()
arr = [[0] * n for _ in range(n)]
ans = 0

# 입력
for i in range(n):
    queries = list(map(int, input().split()))
    for j in range(4):
        # dir 0부터 7까지
        num, dir = queries[j * 2], queries[j * 2 + 1] - 1

        fishes[num] = (i, j, dir)
        arr[i][j] = num

# fish key 로 정렬
fishes = dict(sorted(fishes.items())) # item[0] : key, item[2] : values


# shark 심기 99로 표시
target = arr[0][0]
arr[0][0] = 99
shk = (0, 0)
shark_dir = fishes[target][2]
del fishes[target]
cnt = target
dfs(arr, fishes, shk, shark_dir, cnt)
print(ans)