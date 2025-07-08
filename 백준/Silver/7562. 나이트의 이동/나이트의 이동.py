from collections import deque

t = int(input())
di = [-2, -2, -1, 1, -1, 1, 2, 2]
dj = [-1, 1, 2, 2, -2, -2, -1, 1]

for _ in range(t):
    size = int(input())
    si, sj  = map(int, input().split())
    ei, ej = map(int, input().split())

    arr = [[0] * size for _ in range(size)]
    visited = [[0] * size for _ in range(size)]

    q = deque()
    q.append((si, sj))
    # 초기값 갱신
    arr[si][sj] = 0
    visited[si][sj] = 1
    cnt = 1
    while sum(sum(row) for row in visited) < size * size:

        for _ in range(len(q)):
            ti, tj = q.popleft()

            for k in range(8):
                ni, nj = ti + di[k], tj + dj[k]

                # 범위내, 미방문
                if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj]:
                    arr[ni][nj] = cnt
                    visited[ni][nj] = 1
                    q.append((ni, nj))



        cnt += 1

    print(arr[ei][ej])