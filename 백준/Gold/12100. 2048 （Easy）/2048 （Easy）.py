import sys

sys.setrecursionlimit(100000)  # 필요에 따라 재귀 한도 증가

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_tile = 0

def move_left(board):
    N = len(board)
    new_board = []
    for row in board:
        new_row = []
        temp = [num for num in row if num != 0]
        idx = 0
        while idx < len(temp):
            if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
                new_row.append(temp[idx] * 2)
                idx += 2
            else:
                new_row.append(temp[idx])
                idx += 1
        new_row.extend([0] * (N - len(new_row)))
        new_board.append(new_row)
    return new_board

def move_right(board):
    N = len(board)
    new_board = []
    for row in board:
        new_row = []
        temp = [num for num in row if num != 0][::-1]
        idx = 0
        while idx < len(temp):
            if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
                new_row.append(temp[idx] * 2)
                idx += 2
            else:
                new_row.append(temp[idx])
                idx += 1
        new_row.extend([0] * (N - len(new_row)))
        new_row = new_row[::-1]
        new_board.append(new_row)
    return new_board

def move_up(board):
    transposed_board = [list(row) for row in zip(*board)]
    moved_board = move_left(transposed_board)
    new_board = [list(row) for row in zip(*moved_board)]
    return new_board

def move_down(board):
    transposed_board = [list(row) for row in zip(*board)]
    moved_board = move_right(transposed_board)
    new_board = [list(row) for row in zip(*moved_board)]
    return new_board

def dfs(board, depth):
    global max_tile
    max_tile = max(max_tile, max(map(max, board)))
    if depth == 5:
        return
    for move in [move_left, move_right, move_up, move_down]:
        new_board = move(board)
        if new_board != board:
            dfs(new_board, depth + 1)

dfs(board, 0)
print(max_tile)
