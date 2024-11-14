def rotate(cmd):
    global dice
    # 동쪽 1
    if cmd == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서쪽
    elif cmd == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

    elif cmd == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    elif cmd == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


n, m, i, j, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmd_list = list(map(int, input().split()))
dice = [0] * 6

# 동 서 북 남
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
for cmd in cmd_list:
    # 먼저 dice 이동
    ni, nj = i + di[cmd], j + dj[cmd]

    # 범위 이탈 ->  continue
    if not (0 <= ni < n and 0 <= nj < m):
        continue

    # 범위내라면 i, j 갱신
    i, j = ni, nj

    # cmd에 따라 회전
    rotate(cmd)

    # 바닥이 0 이라면
    if arr[i][j] == 0:
        arr[i][j] = dice[5]

    # 바닥이 0이 아니면
    else:
        dice[5] = arr[i][j]
        arr[i][j] = 0

    print(dice[0])




