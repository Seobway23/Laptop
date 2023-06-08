import sys
from collections import deque
sys.stdin = open('input.txt')
def bfs(y,x):
    # dist cnt 배열 추가, 여기다 넣는 이유: 갱신하기 위해
    visited = [[0] * N for _ in range(N)]

    #초기값 설정
    visited[y][x] = 1
    queue = deque([[y, x]])
    candidate = []

    while queue:
        cy, cx = queue.popleft()
    #4방향 탐색
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            #범위내, 미방문
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if arr[y][x] > arr[ny][nx] and arr[ny][nx] != 0:
                    # dist 추가
                    visited[ny][nx] = visited[cy][cx] + 1
                    # 후보 추가
                    candidate.append((visited[ny][nx] - 1, ny, nx))

                elif arr[ny][nx] == arr[y][x] or arr[ny][nx]==0:
                    # dist 추가
                    visited[ny][nx] = visited[cy][cx] + 1
                    # q추가
                    queue.append([ny, nx])

    return sorted(candidate, key=lambda x: (x[0],x[1], x[2]))

# 방향
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

# input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 기본 값
ans = 0
shark_size = 2
shark_eat = 0

# 처음 시작값 sy, sx 최솟값
for i in range(N):
    for j in range(N):
        if arr[i][j] ==9:
            sy = i
            sx = j

'''
물고기먹는 방법
가장 가까운 고기
물고기 칸이 이동할 때 최솟값이 ans += dist
가장 위, 그다음 가장 왼쪽
-> sort -> dist, y, x 
'''

while True:
    arr[sy][sx] = shark_size

    fish_list = deque(bfs(sy, sx))

    if not fish_list:
        break

    dist, yy, xx = fish_list.popleft()

    # 상어 먹을 것 추가
    shark_eat += 1
    ans += dist

    # 크기 커지는 지 확인
    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

    # 상어 위치 갱신
    arr[sy][sx] = 0
    sy = yy
    sx = xx

print(ans)