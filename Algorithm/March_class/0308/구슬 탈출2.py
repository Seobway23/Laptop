'''
N, M 보드 크기
R 구슬이 O에 들어갈 때 까지의 횟수 구하기
R과 B는 겹치면 안됨
B가 O에 들어가면 return -1
10번이 넘어가도 return -1
'''

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
'''
sys import를 통한 input.txt를 읽기로 불러옵니다.
여기에서 우리는 collections의 내장함수인 deque를 이용해 효율적 q 관리를 할 것입니다.
일반적으로 BFS에서는 deque를 쓸 수 있습니다.
'''

n, m = map(int, input().split()) #n 행, m 열
arr = [ list(input()) for _ in range(n)] # m크기의 input을 n행 만큼 받기
'''
여기서 우리는 보드의 배열을 arr로 받아 줍니다. list comprehension을 이용해 간단하게 표현할 수 있습니다.
또한 스트링으로 인풋을 받는 경우와 list로 인풋을 받는 경우의 시간복잡도는 별로 차이나지 않습니다.
원본 배열을 바꾸는 경우에 list가 효과적이지만 별로 권하진 않기 때문에, 여기에서는 편의상 list로 바꾸고, 방문한 경우는 따로 리스트를 만들어 추가하겠습니다.
'''

v= []
di = [-1,1,0,0]
dj = [0,0,-1,1]
q = deque()


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri, rj = i, j

        if arr[i][j] =='B':
            bi, bj = i, j

q.append((ri, rj, bi, bj, 1)) #cnt -> 1을 q에 추가
v.append((ri, rj, bi, bj))


# dot_search(i,j,di,dj)
def dot_search(i, j, di, dj):
    count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while arr[i + dj][i + dj] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        count += 1
    return i, j, count

def BFS():
    while q:
        ri, rj, bi, bj, cnt = q.popleft()
        # 종료조건 10 이상이면 while문 종료
        if cnt > 10:
            break
        for i in range(len(di)):  # 4방향 탐색
            # R 다음 좌표 nri, nrj, 움직인 거리 r_cnt
            nri, nrj, r_cnt = dot_search(ri, rj, di[i], dj[i])
            # B 다음 좌표 nbi, nbj, 움직인 거리 b_cnt
            nbi, nbj, b_cnt = dot_search(bi, bj, di[i], dj[i])

            #만약 파란 구슬이 구멍을 만나면 continue
            if arr[nbi][nbj] == 'O':
                continue
            #만약 빨간 구슬이 구멍을 만나면
            if arr[nri][nrj] == 'O':
                print(cnt)
                return

            if nri == nbi and nrj == nbj:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_cnt > b_cnt:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    nri -= di[i]
                    nrj -= dj[i]
                else:
                    nbi -= di[i]
                    nbj -= dj[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not (nri, nrj, nbi, nbj) in v:
                v.append((nri, nrj, nbi, nbj))
                q.append((nri, nrj, nbi, nbj, cnt + 1))
    print(-1)  # 실패

BFS()
