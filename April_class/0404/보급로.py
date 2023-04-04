import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

'''
DFS 절대 불가능
왜냐하면 최대 100*100
가장 짧은 경로 -> 라는 말은 뭐다? 갱신 가능 -> 4방향 탐색
'''

# 처음 짠 코드 ->  이렇게 짜게 되면, 뭐가 문제냐면, 불필요한 부분까지 또 탐색해야 함,
# 거의 back tracking 하는 느낌

# def bfs(si,sj,ei,ej):
#     q = deque()
#     q.append((si, sj))
#
#     while q:
#         t = q.popleft()
#         #4 방향 탐색
#         for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#             ni, nj = t[0] + di, t[1] + dj
#
#             if 0<=ni<N and 0<=nj<N:
#                 # 미방문 일 때
#                 if v[ni][nj]==0:
#                     v[ni][nj] = v[t[0]][t[1]] + arr[ni][nj]
#                     q.append(((ni, nj)))
#
#                 # 갱신해야 할 때
#                 elif v[ni][nj] > v[t[0]][t[1]] + arr[ni][nj]:
#                     v[ni][nj] = v[t[0]][t[1]] + arr[ni][nj]
#
#     return v[ei][ej]
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     v = [[0]*N for _ in range(N)]
#     ans = bfs(0,0,N-1,N-1)
#     print(f"#{test_case} {ans}")


def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        t = q.popleft()
        #4 방향 탐색
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = t[0] + di, t[1] + dj

            # 범위내, 누적값보다 더 작을 때,
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[t[0]][t[1]] + arr[ni][nj]:
                    v[ni][nj] = v[t[0]][t[1]] + arr[ni][nj]
                    q.append(((ni, nj)))

    return v[ei][ej]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    INF = 10*N*N
    v = [[INF]*N for _ in range(N)]
    ans = bfs(0,0,N-1,N-1)
    print(f"#{test_case} {ans}")
