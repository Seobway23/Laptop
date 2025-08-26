from collections import deque


def select(arr):
    flag = False
    booms = []
    v = [[0] * 6 for _ in range(12)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] != '.':
                # v, tmp
                tmp = []
                cur_color = arr[i][j]

                # q 추가, 방문 추가
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                tmp.append((i, j))

                while q:
                    ci, cj = q.popleft()

                    # 4방향 탐색
                    for di ,dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ni, nj = ci + di, cj + dj

                        # 미방문, 같은 거라면 추가
                        if 0 <= ni < n and 0 <= nj < m and cur_color == arr[ni][nj] and v[ni][nj] == 0:
                            # q 추가, v 추가, tmp 추가
                            q.append((ni, nj))
                            v[ni][nj] = 1
                            tmp.append((ni, nj))

                if len(tmp) > 3:
                    booms.append(tmp)

    if booms:
        flag = True

    return flag, booms

def boom(lst):
    for color in lst:
        for bi, bj in color:
            arr[bi][bj] = '.'
    return

def drop():
    new_arr = [['.'] * 6 for _ in range(12)]
    # 밑으로 drop . 이 아닌 거만 다 모아서 밑에서 부터 채우기
    for j in range(m):
        tmp = []
        for i in range(n):
            if arr[i][j] != '.':
                tmp.append(arr[i][j])

        # 갱신
        tmp.reverse()
        for k in range(len(tmp)):
            new_arr[11- k][j] = tmp[k]

    return new_arr


n, m = 12, 6
arr = [list(input()) for _ in range(n)]

isBoom = True
step = 0
while isBoom:
    isBoom, boom_lst = select(arr)

    if isBoom:
        boom(boom_lst)
        arr = drop()

    else:
        break

    # 살아남았다는 건, 강하다는 것 step + 1
    step += 1


print(step)