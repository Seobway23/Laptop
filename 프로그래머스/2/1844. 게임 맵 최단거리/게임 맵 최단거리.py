from collections import deque


def solution(maps):
    answer = 1
    col = len(maps)
    row = len(maps[0])
    visited = [ [0] * row for _ in range(col)]
    di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append([0, 0])
    # BFS 돌기
    i, j = 0, 0
    t = 1
    while q:
        for _ in range(t):
            i, j = q.popleft()
            # print(i, j, q)

            if i == col - 1 and j == row - 1:
                return answer

            for k in range(4):
                ni, nj = i + di[k], j + dj[k]

                # 범위내 및 미 방문이면
                if 0 <= ni < col and 0 <= nj < row and not visited[ni][nj] and maps[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
                    pass

        t = len(q)
        answer += 1

    # 도달 하지 못하면
    return -1
