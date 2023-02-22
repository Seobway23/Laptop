'''
arr 배열
for문 4방향 -> 1이라면 cnt+1
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N)]
    sm = N * N # 가장 작은 넘버
    cnt = 0 # 카운트 변수
    for i in range(N):
        for j in range(N):
            #큐를 이용해 cnt
            queue = []
            visited = []
            queue.append((arr[i][j], i, j))
            visited.append((arr[i][j], i, j))
            while queue:
                t = queue.pop()
                for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                    ti =int(t[1])
                    tj =int(t[2])
                    ni = ti + di
                    nj = tj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[ti][tj] == 1:
                        queue.append((arr[ni][ni], ni, nj))
                        visited.append((arr[ni][nj], ni, nj))


            #카운트가 가장 크면서
            if cnt < len(visited):
                cnt = len(visited)
                # 가장 작은 문 숫자이면 갱신
                if sm > arr[i][j]:
                    sm = arr[i][j]

    print(f'#{test_case} {sm} {cnt}')






