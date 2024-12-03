def move(lst):
    global arr
    new_lst = []
    for i, j, d in lst:
        # 8 방향 탐색   # 0: ←, 1: ↖, 2: ↑, 3: ↗, 4: →, 5: ↘, 6: ↓, 7: ↙

        for k in range(8):
            fd = ((d - k) + 8 ) % 8
            ni, nj = i + dir[fd][0], j + dir[fd][1]

            # 범위내, 상어 X , 물고기 냄새 X
            if 0 <= ni < 4 and 0 <= nj < 4 and not fish_smells[ni][nj] and (si, sj) != (ni, nj):
                # move
                new_lst.append((ni, nj, fd))
                arr[ni][nj].append(fd)
                break

        # 이동 불가능 하다면 그대로
        else:
            new_lst.append((i, j, d))
            arr[i][j].append(d) # 2가지라 항상 arr, new_lst에 추가해야 함

    return new_lst


def dfs(si, sj, lst, dfs_lst, fish, v, arr):
    if len(lst) == 3:
        dfs_lst.append([fish] + lst)
        return

    # 상 좌 하 우
    for k, (di, dj) in enumerate(shk_dir):
        ni, nj = si + di, sj + dj
        # 범위내
        if 0 <= ni < 4 and 0 <= nj < 4:
            if not v[ni][nj]:
                # 해당 칸에 있는 모든 물고기의 수를 누적
                fish_cnt = len(arr[ni][nj])

                arr_backup = arr[ni][nj]
                arr[ni][nj] = []  # 물고기 제거
                v[ni][nj] = 1  # 방문 표시

                dfs(ni, nj, lst + [k], dfs_lst, fish + fish_cnt, v, arr)

                # 상태 복구
                v[ni][nj] = 0
                arr[ni][nj] = arr_backup
            else:
                # 이미 방문한 칸이면 물고기를 누적하지 않고 이동만 진행
                dfs(ni, nj, lst + [k], dfs_lst, fish, v, arr)


def shark_move(si, sj):
    global arr, fish_smells
    dfs_lst = []
    v  = [[0] * 4 for _ in range(4)]
    # print(arr)
    dfs(si, sj,[], dfs_lst, 0, v, arr)

    dfs_lst.sort(key= lambda x : (-x[0], x[1], x[2], x[3]))
    # 이동할 리스트
    # print("ㅇㅇㅇ 리스트: ", si, sj, dfs_lst)
    sharks_moves = dfs_lst[0]
    # print("이동할 리스트: ", sharks_moves)
    for k in sharks_moves[1:]:
        # print("K:", k)
        ni, nj = si + shk_dir[k][0], sj + shk_dir[k][1]
        if len(arr[ni][nj]) > 0:
            fish_smells[ni][nj] = 2 + 1  # 3 카운트 -> 바로 하나 -1 해야 함
            arr[ni][nj] = []  # 빈 배열
        # 상어 위치 갱신
        # print("위치 갱신: ", (si, sj) , (ni, nj))
        si, sj = ni, nj


    return si, sj


def find():
    global arr
    new_lst = []
    for i in range(4):
        for j in range(4):
            if len(arr[i][j]) > 0:
                for d in arr[i][j]:
                    new_lst.append((i, j, d))


    return new_lst


# init
m, s = map(int, input().split())
# 1, 1 => 0, 0, 으로 변경
fish_lst = []
# 0: ←, 1: ↖, 2: ↑, 3: ↗, 4: →, 5: ↘, 6: ↓, 7: ↙
dir = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),  (1, -1))
shk_dir = ((-1, 0), (0, -1), (1, 0), (0, 1))    # 0: ↑, 1: ←, 2: ↓, 3: →
# 물고기 냄새
fish_smells = [[0] * 4 for _ in range(4)]


for _ in range(m):
    fi, fj, d = map(int, input().split())
    # 방향, i, j 모두 -1 해줘야 함
    fish_lst.append((fi - 1, fj - 1, d - 1))

# 상어 위치
si, sj = map(lambda x : int(x) - 1, input().split())


for _ in range(s):
    arr = [ [[] for _ in range(4)] for _ in range(4)]   # 배열 -> 턴 마다 갱신

    # 1. 복제
    fish_copy = [row[:] for row in fish_lst]
    # print(fish_copy)

    # 2. 물고기 이동
    new_lst = move(fish_lst)
    # print("이동:", arr)

    # 3. 상어 이동
    si, sj = shark_move(si, sj)

    # 4. 냄새 -1
    for i in range(4):
        for j in range(4):
            if fish_smells[i][j] > 0:
                fish_smells[i][j] -= 1

    # print("복전: ", arr, (si, sj))

    # 5. 복제한 물고기 추가
    for i, j, d in fish_copy:
        arr[i][j].append(d)

    # fish_copy 갱신
    fish_lst = find()
    # print("복후: ", arr)
    # print()

# ans 출력
ans = sum(len(x) for sub_arr in arr for x in sub_arr)
print(ans)
