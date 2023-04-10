'''
1. Start 지점 찾기
2. 탐색 시작
    1) 시작 지점, 큐 v 추가
    2) 0이면서 미방문
    - 큐, V 추가
3. 도착하면 1
    끝나면 0

'''


import sys
sys.stdin = open('input.txt', 'r')

def BFS(arr, S):
    #초기 값 설정
    v = [[0]*N for _ in range(N)]
    queue = []

    #시작 지점, 큐,v 추가
    queue.append(S)
    v[S[0]][S[1]] = 1

    #탐색 시작
    while queue:
        t = queue.pop()
        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
            ni = t[0]+di
            nj = t[1]+dj

            # 종료 조건, 3 찾으면 바로 return 1
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 3:
                return 1

            # 범위 안에서, 조건이 맞으면 큐, v 추가
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and v[ni][nj] == 0:
                queue.append((ni, nj))
                v[ni][nj] = 1

    return 0


T = 10 #int(input())
for test_case in range(1, T+1):
    tc = int(input())
    N = 16 #문제는 13
    arr = [list(map(int, input())) for _ in range(N)]
    #시작 위치
    S = (1, 1)

    print(f'#{tc} {BFS(arr, S)}')