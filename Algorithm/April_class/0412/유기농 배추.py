import sys
sys.stdin = open('input.txt', 'r')


def search(i,j):
    global ans
    di = [0,0,-1,1]
    dj = [-1,1,0,0]
    q = []
    q.append((i,j))

    dd = arr
    while q:
        t = q.pop(0)
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0<=ni<M and 0<=nj<N and arr[ni][nj]:
                q.append((ni,nj))
                arr[ni][nj] = 0

    ans += 1



    return

T = int(input())
for test_case in range(1, T+1):
    N, M, D = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for _ in range(D):
        bi, bj = map(int, input().split())
        arr[bj][bi] = 1
    ans = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                search(i, j)

    print(ans)
