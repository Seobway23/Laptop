import sys
sys.stdin = open('input.txt', 'r')

'''
중복 방문을 포함하는 BFS 변형 형태
중복 방문을 위해 상하좌우 탐색
'''

def bfs(si, sj, ei, ej):
    INF = 10*N*N

    q = []
    v = [[INF]*N for _ in range(N)]

    # q, v 추가
    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)
        # 목적지라고 여기서 return X .. (중복 방문)

        # 4방향, 범위내, 이동할 위치 누적값보다 더 작은 값일 경우 갱신
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0,0,N-1,N-1)
    print(f'#{test_case} {ans}')
