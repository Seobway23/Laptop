#1 import
import sys
sys.stdin = open('input.txt','r')

from collections import deque


#2 입력 받기
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

#3 기본값 지정
di = [-1,0,1,0]
dj = [0,1,0,-1]
v = []
q = deque()
cnt = 1
#cnt를 1로 하는 이유는 마지막에 R이 O를 만날 때 cnt+=1을 안하기 때문에 1을 추가한다

#4 초기값 지정 -> 초기 R, B 값 지정
def init(): #구조화 중요

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R': #R 찾으면 ri, rj 저장
                ri, rj = i, j
            elif arr[i][j] == 'B': #B 찾으면 bi, bj 저장
                bi, bj = i, j
    #v, q에 추가
    v.append((ri,rj,bi,bj)) #visited는 좌표값만 추가
    q.append((ri,rj,bi,bj,cnt)) #cnt를 세야 하기 때문에 q에 cnt 0 추가


#5 동작할 함수 지정 -> 길 이동
def road_search(i,j, di, dj):
    road = 0  # 이동 칸수
    #다음 위치가 벽이 아닐 때/ 지금 위치가 O가 아닐 때,
    while arr[i+di][j+dj] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        road += 1
    return i, j, road


#6 BFS 시작
def BFS():
    init()
    # q 와 while 로 BFS 시작
    while q:
        ddd= q
        dd = v
        d= arr
        ri, rj, bi, bj, cnt = q.popleft()
        # 종료 조건 10을 초과하면 -1 return 이므로 break
        if cnt > 10:
            break
#while q 안에 방향 탐색 시작
        for k in range(len(di)): # 0, 1, 2, 3 4방향/ 코드 가독성을 위해 len(di)
            rni, rnj, r_cnt = road_search(ri,rj,di[k],dj[k])
            bni, bnj, b_cnt = road_search(bi,bj,di[k],dj[k])

            #파란공 O 도착 여부
            if arr[bni][bnj] == 'O':
                continue
            #빨간공 O 도착 여부
            if arr[rni][rnj] == 'O':
                return cnt

            #중복 공 제거
            if rni == bni and rnj == bnj: #동시에 있으면 중복 제거해야 함
                if r_cnt > b_cnt:
                    rni -= di[k]
                    rnj -= dj[k]
                else:
                    bni -= di[k]
                    bnj -= dj[k]

            #미방문 표시
            if not (rni,rnj,bni,bnj) in v:
                q.append((rni,rnj,bni,bnj,cnt+1))
                v.append((rni,rnj,bni,bnj))

    return -1

print(BFS())
