N, K = map(int, input().split())

# 입력, 패딩 추가
raw = [list(map(int, input().split())) for _ in range(N)]
board_color = [[2] * (N + 2)]                        
for row in raw:
    board_color.append([2] + row + [2])
board_color.append([2] * (N + 2))            


# 저장
board = [[[] for _ in range(N + 2)] for _ in range(N + 2)]

pieces = []
for i in range(K):
    r, c, d = map(int, input().split())
    d -= 1
    pieces.append([r, c, d])
    board[r][c].append(i)

# 방향 벡터
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 방향 반전
def rev(d):
    if d == 0: return 1
    if d == 1: return 0
    if d == 2: return 3
    if d == 3: return 2


turn = 1
while turn <= 1000:
    for i in range(K):
        r, c, d = pieces[i]

        # 현재 칸의 스택에서 i의 위치 찾기
        idx = board[r][c].index(i)
        moving = board[r][c][idx:]      # i 포함 위쪽 스택
        board[r][c] = board[r][c][:idx] # 남는 아래 스택

        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 칸이 파란색이면 반전
        if board_color[nr][nc] == 2:
            d = rev(d)
            pieces[i][2] = d            # 방향 반전 기록

            nr = r + dr[d]
            nc = c + dc[d]

            # 반전 후에도 파란색이면 제자리로 복귀
            if board_color[nr][nc] == 2:
                board[r][c].extend(moving)
                continue

        #흰색
        if board_color[nr][nc] == 0:
            board[nr][nc].extend(moving)

        #  빨간색: reverse
        elif board_color[nr][nc] == 1:
            board[nr][nc].extend(moving[::-1])

        # 이동 말 위치 갱신
        for m in board[nr][nc]:
            pieces[m][0] = nr
            pieces[m][1] = nc

        # 종료 조건 : 스택 4개 이상
        if len(board[nr][nc]) >= 4:
            print(turn)
            exit()

    turn += 1

print(-1)