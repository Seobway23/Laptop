import sys
sys.stdin=open("input.txt", "r")

def stk_arr(arr):
    # 각 초깃값 만들기
    stk=[]
    ci, cj= si, sj #기준점 저장
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 위, 아래, 왼쪽, 오른쪽

    # 미로 찾기 시작
    while True:  # while문으로 카운팅하지 않고 찾으면 break를 함
        #1 아니면 탐색
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            if visited[ni][nj]==0 and arr[ni, nj]!=1:
                stk.append((ci,cj))

                ci, cj = ni, nj
                visited[ci][cj]=1
                break


        else:
            if stk:
                ci, cj = stk.pop()

            else:
                break


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    #배열 만들기
    arr=[[1]*(N+2)]
    for _ in range(N):
        arr_1=list(map(int,input())) #split만 빼면 됨
        arr.append([1]+arr_1+[1])
    arr.append([1]*(N+2))

    visited=[[0]*(N+2) for _ in range(N+2)]

    # start, end 찾기
    for i in range(1, N+1):  # 원래 배열이 1부터 N까지 이므로 0은 고려하지 않아도 됨
        for j in range(1, N+1):
            if arr[i][j] == 2:
                si, sj= i, j
            if arr[i][j] == 3:
                ei, ej= i, j

        #각 초깃값 만들기

    stk_arr(arr) #def stk_arr 만들기






    print(f"#{test_case} {ans}")