def move_left(board):
    N = len(board)
    merge = []
    for row in board:
        new_row = []
        tiles = [num for num in row if num != 0]
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                new_row.append(tiles[i] * 2)
                i += 2
            else:
                new_row.append(tiles[i])
                i += 1
        new_row.extend([0] * (N - len(new_row)))
        merge.append(new_row)
    return merge

def move_right(board):
    N = len(board)
    merge = []
    for row in board:
        new_row = []
        tiles = [num for num in row if num != 0][::-1]
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                new_row.append(tiles[i] * 2)
                i += 2
            else:
                new_row.append(tiles[i])
                i += 1
        new_row.extend([0] * (N - len(new_row)))
        merge.append(new_row[::-1])
    return merge

def move_up(board):
    trans_board = [list(row) for row in zip(*board)]
    new_board = move_left(trans_board)
    merge = [list(row) for row in zip(*new_board)]
    return merge

def move_down(board):
    trans_board = [list(row) for row in zip(*board)]
    new_board = move_right(trans_board)
    merge = [list(row) for row in zip(*new_board)]
    return merge

def dfs(board, depth):
    global max_tile
    max_tile = max(max_tile, max(map(max, board)))
    # 종료 조건
    if depth == 5:
        return

    # 4방향 탐색
    for move in [move_left, move_right, move_up, move_down]:
        new_board = move(board)

        if new_board != board:
            dfs(new_board, depth + 1)

    return

# 초기값 input
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_tile = 0
dfs(board, 0)
print(max_tile)
