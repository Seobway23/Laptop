import math
from collections import deque

# 인구 이동이 끝날 째 까지 반복
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
flag = True
ans = 0

def search():
    searches = []
    v = [[0] * n for _ in range(n)]
    # 리스트 찾기
    # i, j 를 돌면서 v -> 각각의 리스트 확인
    for i in range(n):
        for j in range(n):
            lst = []
            # 미방문 이면 일단 표시
            if not v[i][j]:
                q = deque()
                lst.append((i, j))
                v[i][j] = 1
                q.append((i,j))

                # BFS 돌면서
                while q:
                    ci, cj = q.popleft()
                    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ni, nj = ci + di, cj + dj

                        # 미방문, 범위내, 조건 만족
                        if 0 <= ni < n and 0 <= nj < n  and not v[ni][nj]:
                            if l <= abs(arr[ci][cj] - arr[ni][nj]) <= r:
                                # q 추가, 방문 표시, lst 추가
                                q.append((ni, nj))
                                v[ni][nj] = 1
                                lst.append((ni, nj))

            if len(lst) > 1:
                searches.append(lst)

    # print("하위:",searches)
    return searches


def move(lst):
    # print("무브, arr:", arr)
    new_flag = True
    # lst 가 있으면 True, 이동
    if lst:

        for cur in lst:
            cur_sm = sum(arr[mi][mj] for mi, mj in cur)
            cur_num = math.trunc(cur_sm / len(cur))

            # 이제 갱신
            for ci, cj in cur:
                arr[ci][cj] = cur_num
        # print(arr)

    # lst 없으면 반환
    else:
        new_flag = False


    return arr,new_flag


while flag:
    lst = search()
    arr, flag = move(lst)

    if flag:
        ans += 1

print(ans)