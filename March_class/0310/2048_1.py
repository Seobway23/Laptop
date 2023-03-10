'''
move 함수 만들기
# 튜플을 리스트로 바꾸는 법
my_list = [list(x) for x in my_list]
#print(my_list)
a = list(map(list, my_list))

dfs 함수 시작

1. for k -> 4방향
    1) move 했는데, 움직였어?
        대신에 무브 함수는 -> 움직이면 arr 바뀌는 것까지 해야 해
        그러면 재귀 함수호출
    2) 안움직인다?
        continue

2. 다했으면 mx 갱신

'''

import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx1 = 0
ans = []
cnt = 0

def mx(mx1):
    for ni in range(N):
        for nj in range(N):
            if arr[ni][nj] > mx1:
                mx1 = arr[ni][nj]

#move 함수 구현 완료
def move_right(arr, N1):

    if N1 == 5:
        mx(mx1)
        ans.append(mx1)
        return
    N1 += 1

    cnt = 0
    # 오른쪽 진행
    for i in range(N):
        j = N-1; v=[]
        while j > -1:
            if 1<= j-1 <N and arr[i][j] == arr[i][j-1] and arr[i][j]:
                num = arr[i][j] + arr[i][j-1]
                arr[i][j] = 0
                arr[i][j - 1] = 0
                v.append(num)
                cnt += 1
                j -= 2

            else:
                v.append(arr[i][j])
                j -= 1
        #while문이 끝나면
        else:
            arr_t = [0] * N
            #만약 움직였으면,

            for ni in range(len(v)):
                arr_t[N-1-ni] = v[ni]

            for nj in range(len(arr_t)):
                arr[i][nj] = arr_t[nj]


    # 종료조건
    if cnt == 0:
        return

    else:
        recursion(N1+1)

    return

def move_left(arr, N1):
    if N1 == 5:
        mx(mx1)
        ans.append(mx1)
        return
    N1 += 1

    # 왼쪽 진행
    cnt = 0
    for i in range(N):
        j = 0; v=[]

        while j < N:
            d = cnt
            if 1 <= j+1 < N and arr[i][j] == arr[i][j+1] and arr[i][j]:

                num = arr[i][j] + arr[i][j+1]
                arr[i][j] = 0
                arr[i][j + 1] = 0
                v.append(num)
                j += 2
                cnt += 1

            else:
                v.append(arr[i][j])
                j += 1


        # while 문이 끝나면
        arr_t = [0]*N

        # 만약 움직였으면,
        for ni in range(len(v)):
            arr_t[ni] = v[ni]

        for nj in range(len(arr_t)):
            arr[i][nj] = arr_t[nj]

    # 종료조건
    if cnt:
        recursion(N1+1)

    else: #cnt 가 0 이면,
        return

    return

def move_top(arr, N1):

    if N1 == 5:
        mx(mx1)
        ans.append(mx1)
        return
    N1 += 1

    cnt = 0
    # 위쪽 진행
    arr_v = list(map(list, list(zip(*arr))))

    for i in range(N):
        j = 0; v=[]

        while j < N:
            if 0 <= j+1 < N and arr_v[i][j] == arr_v[i][j+1] and arr_v[i][j]:
                num = arr_v[i][j] + arr_v[i][j+1]
                arr_v[i][j] = 0
                arr_v[i][j + 1] = 0
                v.append(num)
                j += 2
                cnt += 1

            else:
                v.append(arr_v[i][j])
                j += 1

        # while문이 끝나면
        arr_t = [0]*N

        # 만약 움직였으면,
        for ni in range(len(v)):
            arr_t[ni] = v[ni]

        for nj in range(len(arr_t)):
            arr[nj][i] = arr_t[nj]

    # 종료조건
    if cnt == 0:
        return

    else:
        recursion(N1+1)

    return
def move_bottom(arr, N1):

    if N1 == 5:
        mx(mx1)
        ans.append(mx1)
        return
    N1 += 1

    cnt = 0
    # 아래쪽 진행
    arr_v = list(map(list, list(zip(*arr))))
    for i in range(N):
        j = N-1; v=[]
        while j > -1:
            if 0<= j-1 <N and arr_v[i][j] == arr_v[i][j-1]:
                num = arr_v[i][j] + arr_v[i][j-1]
                arr_v[i][j] = 0
                arr_v[i][j - 1] = 0
                v.append(num)
                j -= 2
                cnt += 1

            else:
                v.append(arr_v[i][j])
                j -= 1

        # while문이 끝나면
        else:
            arr_t = [0]*N

            #만약 움직였으면,
            for ni in range(len(v)):
                arr_t[N-1-ni] = v[ni]

            for nj in range(len(arr_t)):
                arr[nj][i] = arr_t[nj]

    # 종료조건
    if cnt == 0:
        return

    else:
        recursion(N1+1)

    return

# 문제가 지금 -> 바꾼 거를 입력하지 않음

#움직이지 않으면 X라는 것을 구현 못했음

# 재귀 함수 구현
cnt = 0
def recursion(N):
    move_left(arr,N)
    move_top(arr,N)
    move_bottom(arr,N)
    move_right(arr, N)


recursion(0)
print(ans)


