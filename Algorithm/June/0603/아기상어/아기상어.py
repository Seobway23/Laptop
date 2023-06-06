'''
1. 먹을 물고기 없으면 끝
2. 먹을 물고기가 한마리라면 그것만 먹으러가기
3. 2마리라면 가까운 물고기 먹으러 가기(칸의 최솟값)

배열 인풋
돌면서, i, si, sj 값 좌표 -> i sort
상어좌표랑 차이나는 것 -> 가장 작은 곳 ->
'''
import sys
from collections import deque
sys.stdin = open('input.txt')


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sy = i
            sx = j

cnt = 0


# 3. 가까운 먹이를 찾는 탐색 문제이기 때문에 `BFS`를 생각해 볼 수 있다.
# 4. BFS를 사용할 시 입력으로는 현재 아기 상어의 위치를 생각할 수 있고,
# 	 출력으로는 후보를 리스트를 반환 해야한다.
def bfs(y, x):
    # y, x는 현재 위치에서 BFS
    # visited는 거리 메모 테이블
    visited = [[0] * N for _ in range(N)]
    queue = deque([[y, x]])
    cand = []

    visited[y][x] = 1

    while queue:
        cy, cx = queue.popleft()

        for i in range(4):# 4방향 탐색
            ny, nx = cy + dy[i], cx + dx[i]
            # 범위내, 미방문일 떄
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:

                # 먹을 수 있을 때
                if space[y][x] > space[ny][nx] and space[ny][nx] != 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    # 후보에 추가 // 처음에 visited +1을 해줬으니 -1해줘야 함
                    cand.append((visited[ny][nx] - 1, ny, nx))

                # 만약 같거나, 방문지가 0이라면, queue에 넣어서 탐색
                elif space[y][x] == space[ny][nx] or space[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append([ny, nx])

    # 우선순위에 따른 리스트 정렬 후 return// 0 거리, 1 y축, 2 x축
    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


size = [2, 0]
# 8. 맨 앞의 후보만 먹고 위치 이동후 다시 BFS 해야한다
while True:
    space[sy][sx] = size[0]
    cand = deque(bfs(sy, sx))

    if not cand:
        break

    # 7. 후보리스트가 나오면 맨 앞의 후보 먹이를 뽑아 그 위치로 이동한다.
    step, yy, xx = cand.popleft()
    cnt += step
    size[1] += 1

    # 9. 몇 개를 먹었는지 몇 초간 이동했는지 체크해 줄 필요가 있다.
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[sy][sx] = 0
    sy, sx = yy, xx

print(cnt)