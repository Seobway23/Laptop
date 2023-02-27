'''
범위내 미방문, 조건
위 -> 아래 , 상 하 좌우 counter맞아야 함
상대방의 좌표가 다른 곳의 좌표에 있다면, 추가 스택 쌓기
'''
import sys
sys.stdin = open('input.txt', 'r')

def find(arr):
    i = 1
    dd= v
    qq= q
    while i < L:
        for _ in range(len(q)):
            t = q.pop(0)
            w = t[0]
            ww = t[1]
            num = arr[t[0]][t[1]]
            for j in dic[num]:
                ni = t[0]+dir[j][0]
                nj = t[1]+dir[j][1]
                # and arr[ni][nj] !=0 를 조건으로 넣던가, dic에서 0을 작동하지 않게 조정하거나,
                if 0<= ni < N and 0<= nj < M and arr[ni][nj] !=0 and not (ni,nj) in v:
                    for k in dic[arr[ni][nj]]:
                        if opr[k] in dic[num]:
                            v.append((ni, nj))
                            q.append((ni, nj))
                            break

        i += 1





T= int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) #N 세로, M 가로, R 세로시작, C 가로시작, L 소요시간
    arr = [list(map(int,input().split())) for _ in range(N)]

    #처음시작 위치 v, q 저장
    q = []; v = [];
    v.append((R,C))
    q.append((R,C))

    #direction, 반대 저장
    dir = ((-1,0),(1,0),(0,-1),(0,1))
    #지금 문제가 dic에서 (리스트) 형태로 주어진 것이 아닌, 다른 것으로 주어졌기 때문에
    dic = {0:('9','9'),1:(0,1,2,3), 2:(0,1),3:(2,3),4:(0,3),5:(1,3) ,6:(1,2), 7:(0,2)}
    opr = {0:1, 1:0, 2:3, 3:2,'9':'9'}
    find(arr)
    len(v)
    print(f"#{test_case} {len(v)}")