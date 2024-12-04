def add_smell():
    global arr, smells, cnt
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                smells[i][j] = [arr[i][j], cnt]


def move(i, j, num, k):
    # 냄새가 없다면
    for didx in shk_dir[num][k][1:]:
        ni, nj = i + move_dir[didx][0], j + move_dir[didx][1]
        # 범위내
        if 0 <= ni < n and 0 <= nj < n and not smells[ni][nj][0]:
            return ni, nj, num, didx

    # 냄새가 있다면
    for didx in shk_dir[num][k][1:]:
        ni, nj = i + move_dir[didx][0], j + move_dir[didx][1]
        if 0 <= ni < n and 0 <= nj < n and smells[ni][nj][0] == num:
            return ni, nj, num, didx

    # 못 움직 이면
    return i, j, num, k

# input, 0 padding
move_dir = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)) # 0:원점, 1:상, 2:하, 3:좌, 우
n, m ,cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cur_dir = [0] + list(map(int, input().split()))
shk_dir = [[[0]]] +[[[0]] + [[0] + list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

# init
shk_list =dict()    # (i, j) : (num, dir)
smells = [[[0, 0]] * n  for _ in range(n)]  # [0]: num, [1]: cnt
time = 0

while True:
    # 종료 조건
    if sum(map(sum, arr)) == 1:
        break

    if time >= 1000:
        time = -1
        break

    # 1. 냄새 -1
    for i in range(n):
        for j in range(n):
            if smells[i][j][0]:
                smells[i][j][1] -= 1

                # 0 이면 [0,0] 갱신
                if not smells[i][j][1]:
                    smells[i][j] = [0, 0]

    # 배열 갱신
    new_arr = [[0] * n for _ in range(n)]

    #
    # print("smells: ----------------")
    # pprint(smells)
    # print("------------------------")

    # 1-1. 추가후 shk_list 갱신
    new_shk_list = dict()

    # 2. 동시 이동 i, j 또는 -> sh_list 순회
    for i in range(n):
        for j in range(n):
            if arr[i][j]:   # 있을 때
                ni, nj, num, nk = move(i, j, arr[i][j], cur_dir[arr[i][j]])  # [0]: arr_i, [1]: arr_j, , [2]: num, [3]: 현재 dir
                # print("i: ", ni, ", j:", nj, ", num,:", num,", k:", nk)
                # 겹침 갱신, shk_list
                if (ni, nj) in new_shk_list:
                    if new_shk_list[(ni, nj)][0] > num: # num 이 더 작으면 갱신
                        new_shk_list[(ni, nj)] = (num, nk)

                else:
                    new_shk_list[(ni, nj)] = (num, nk)

    # 3. 냄새 베기, smell 추가,
    add_smell()

    # 4. data 갱신
    # new_arr, cur_dir 갱신
    for (i, j ), (num, dir) in new_shk_list.items():
        new_arr[i][j] = num
        cur_dir[num] = dir

    # arr 이동 후 갱신 해야 함, arr = new_arr
    arr = new_arr
    # print("------------------------")
    # pprint(new_arr)
    # print("------------------------")
    # while 문에서 돌고, 마지막 갱신
    shk_list = new_shk_list

    # 시간 추가
    time += 1


print(time)