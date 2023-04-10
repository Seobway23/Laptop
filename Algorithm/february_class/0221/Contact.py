import sys
sys.stdin = open('input.txt', 'r')

def BFS(arr, S):
    global arr_num
    v = [0] * arr_num
    queue = []

    #시작점 추가
    queue.append(S)
    v[S] = 1

    #탐색 시작
    while queue:
        t = queue.pop(0)
        for j in range(arr_num):
            if arr[t][j] == 1 and v[j] == 0:
                queue.append(j)
                v[j] = v[t] +1

    #마지막 값 읽기
    #최댓값  찾기
    p = []
    mx = 0
    for i in range(len(v)):
        if v[i] >= mx:
            mx = v[i]
            p.append((mx, i))

    #인덱스 최댓값 찾기
    idx = 0
    for i in p:
        if i[0] == mx:
            if i[1] > idx:
                idx = i[1]

    return idx





T = 10
for test_case in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    arr_num = 100 + 1
    arr = [[0] * arr_num for _ in range(arr_num)]

    for i in range(0,N,2): #2간격씩 해서 i, i+1 두개로 쓰기
        arr[lst[i]][lst[i+1]] = 1


    print(f"#{tc} {BFS(arr, S)}")





    #print(f"#{test_case} {BFS(arr, S)}")