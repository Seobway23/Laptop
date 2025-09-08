from collections import deque
from itertools import combinations


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

# 1. 2_후보 고르기
two_lst = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 2]
candidates = combinations(two_lst, m)

# make_new_lst
def make_new_lst(cur_ij_new):
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 2:
                new_arr[i][j] = arr[i][j]

    # 후보 2 갱신
    for i,j in cur_ij_new:
        new_arr[i][j] = 2

    return new_arr

# 4. BFS()
def BFS(new_arr):
    # 초기값 갱신
    v = [[0] * n for _ in range(n)]
    # 벽은 -1 해야 함
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] == 1:
                v[i][j] = -1
    # virus 전파
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] == 2:
                # BFS 시작
                q = deque()
                q.append((i, j, 1)) # 1부터 시작 이므로 cnt 나중에 -1 해줘야 함
                v[i][j] = 1
                while q:
                    ci, cj, c_cnt = q.popleft()
                    if arr[ci][cj] == 2:
                        v[ci][cj] = 1
                        # 이렇게 하면, 방문 표시도 되면서 비활성을 거치는 BFS도  해결 가능

                    # 4 방향 탐색
                    for di, dj in ((0, 1), (0, -1) , (1, 0), (-1, 0)):
                        ni, nj = ci + di, cj + dj
                        # 범위내, 0일 때
                        if 0 <= nj < n and 0 <= ni < n and new_arr[ni][nj] != 1:
                            # 미방문
                            if v[ni][nj] == 0 and new_arr[ni][nj] == 0:
                                q.append((ni, nj, c_cnt + 1))
                                v[ni][nj] = c_cnt + 1

                            # 방문 했지만,
                            else:
                                # cnt 더 적을 때
                                if v[ni][nj] != -1 and v[ni][nj] > c_cnt + 1:
                                    q.append((ni, nj, c_cnt + 1))
                                    v[ni][nj] = c_cnt + 1


    # sns 갱신 빈칸이 있으면 안됨
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 2 and v[i][j] == 0:
                return -1

            else:
                cnt = max(cnt, v[i][j])

    return cnt - 1


# 2. main roof 돌리기
for cur_ij in candidates:
    # 후보만 2로 남기는 lst 만들기
    new_lst = make_new_lst(cur_ij)
    new_cnt = BFS(new_lst)
    if new_cnt != -1:
        ans = min(ans, new_cnt)
print(-1 if ans == float("inf") else ans)