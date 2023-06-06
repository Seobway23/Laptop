import sys
from collections import deque
sys.stdin = open('input.txt')

'''
1. input

2. 움직임
1) 가장 위에 물고기
2) 가장 왼쪽 물고기
3) ans += 1 -> 최종 출력 -> 시간

3. shark
1) size
2) eat
'''

# BFS (가까운 먹이 탐색)
def BFS(y, x):
    # y, x는 현재 위치에서 BFS
    # visited는 거리 메모 테이블
    visited = [[0] * N for _ in range(N)]
    queue = deque([[y, x]])
    cand = []

    visited[y][x] = 1

    while queue:
        cy, cx = queue.popleft()
        for i in range(4):  # 4방향 탐색
            ny, nx = cy + dy[i], cx + dx[i]

            # 범위내, 미방문일 떄
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:

                # 먹을 수 있을 때
                if arr[y][x] > arr[ny][nx] and arr[ny][nx] != 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    # 후보에 추가 // 처음에 visited +1을 해줬으니 -1해줘야 함
                    cand.append((visited[ny][nx] - 1, ny, nx))

                # 만약 같거나, 방문지가 0이라면, queue에 넣어서 탐색
                elif arr[y][x] == arr[ny][nx] or arr[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append([ny, nx])



    # 우선순위에 따른 리스트 정렬 후 return// 0 거리, 1 y축, 2 x축
    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


# input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# sx, sy 찾기 arr[y][x]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sy = i
            sx = j

# 초기값
shark_size = 2
shark_eat = 0
ans = 0

while True:
    # 처음 시작 9를 2로 갱신
    arr[sy][sx] = shark_size
    # 후보 리스트 deque 갱신
    candidate = deque(BFS(sy, sx))
    # print(candidate)
    # print(sy, sx)

    if not candidate:
        break

    # candidate pop
    dist, yy, xx = candidate.popleft()
    ans += dist
    shark_eat += 1

    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

    arr[sy][sx] = 0
    sy, sx = yy, xx

print(ans)









