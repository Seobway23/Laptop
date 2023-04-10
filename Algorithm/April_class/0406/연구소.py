'''
N*M 행렬
3<= N,M<= 8
# [1] 0인 곳 중에 3개를 1로 만들어야 함
-> 3개 세울 곳 모르겠음, 최댓값이면 DFS
-> 시간적 여유 충분함 -> DFS로 구현하면 됨 문제는 first DFS 구현을 어떻게 할 것인가..

# [2] 바이러스 분포 while 0이 아닐때까지, queue
-> 가능

# [3] 0 세기
-> 가능
'''

import sys
sys.stdin = open('input.txt', 'r')

# 어떻게 기둥을 넣을 것인가....


def first(i_1, j_1, i_2, j_2, i_3, j_3, cntd):
    if cntd == 3:
        arr[i_1][j_1] = 1
        arr[i_2][j_2] = 1
        arr[i_3][j_3] = 1
        second(arr)
        third(arr)
        # 되돌리기
        arr[i_1][j_1] = 0
        arr[i_2][j_2] = 0
        arr[i_3][j_3] = 0

    if arr[i_1][j_1] != 0 or arr[i_2][j_2]!=0 or arr[i_3][j_3]!=0:
        return

    if 0<= i_1< N and 0<= i_2< N and 0<= i_3< N and 0<= j_1< M and 0<= j_2< M and 0<= j_3< M:
        first(i_1 +1, j_1, i_2, j_2, i_3, j_3,cntd +1)
        first(i_1, j_1+1, i_2, j_2, i_3, j_3,cntd +1)
        first(i_1, j_1, i_2+1, j_2, i_3, j_3,cntd +1)
        first(i_1, j_1, i_2, j_2+1, i_3, j_3,cntd +1)
        first(i_1, j_1, i_2, j_2, i_3+1, j_3,cntd +1)
        first(i_1, j_1, i_2, j_2, i_3, j_3+1,cntd +1)
    else:
        return



def second(arr):
    second = []
    # 미생물 2 좌표 찾기
    for ti in range(N):
        for tj in range(M):
            if arr[tj][ti] == 2:
                second.append((tj,ti))

    # 시작
    while second:
        ci, cj = second.pop(0)
        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)): # 상 부터 시계방향
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0: # 범위내, 0이라면,
                arr[ni][nj] = 2
                second.append((ni, nj))

def third(arr): # N^2 복잡도
    global ans
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[j][i] == 0:
                cnt += 1

    if ans < cnt:
        ans = cnt
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
second(arr)
first(0, 0, 0, 0, 0, 0, 0)
print(ans)

