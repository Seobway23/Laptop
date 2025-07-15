from collections import deque
import copy
from itertools import combinations


n, m, g, r = map(int, input().split())
# [0]: 호수, [1]: 배양액 X, [2]: 배양액 O
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = 0

'''
1. 배양액 후보를 탐색한다.
2. 배양액을 모두 뿌린다.
3. move를 한다, 
4. 꽃의 개수를 파악한다 
'''

di, dj = [-1, 1, 0, 0], [0, 0, 1, -1]
def move(glst, rlst):
    global ans
    # 1. 도달 시간을 기록할 배열: -1 = 미도달
    timeG = [[-1]*m for _ in range(n)]
    timeR = [[-1]*m for _ in range(n)]
    flower = [[False]*m for _ in range(n)]
    cnt = 0

    # 2. 초기 배양액을 큐에 (i,j,시간,색) 으로 넣기
    q = deque()
    for i,j in glst:
        timeG[i][j] = 0
        q.append((i, j, 0, 'G'))
    for i,j in rlst:
        timeR[i][j] = 0
        q.append((i, j, 0, 'R'))

    # 3. BFS
    while q:
        i, j, t, color = q.popleft()
        # 이미 꽃이 핀 칸이면 스킵
        if flower[i][j]:
            continue

        # 4방 탐색
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            nt = t + 1

            # 범위·호수·꽃 검사
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if arr[ni][nj] == 0 or flower[ni][nj]:
                continue

            if color == 'G':
                # 초록이 이미 왔으면 스킵
                if timeG[ni][nj] != -1:
                    continue
                # 초록 도달 시간 기록
                timeG[ni][nj] = nt

                # 빨강도 같은 시간에 왔으면 꽃
                if timeR[ni][nj] == nt:
                    cnt += 1
                    flower[ni][nj] = True
                # 아니면 초록만 차지 → 다음으로 전파
                elif timeR[ni][nj] == -1:
                    q.append((ni, nj, nt, 'G'))

            else:  # color == 'R'
                if timeR[ni][nj] != -1:
                    continue
                timeR[ni][nj] = nt

                if timeG[ni][nj] == nt:
                    cnt += 1
                    flower[ni][nj] = True
                elif timeG[ni][nj] == -1:
                    q.append((ni, nj, nt, 'R'))

    # 4. 최대값 갱신
    ans = max(ans, cnt)

cands = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 2]

for green in combinations(cands, g):
    rem = set(cands) - set(green)
    for red in combinations(rem, r):
        move(list(green), list(red))

print(ans)