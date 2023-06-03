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

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2
# 상어위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


def biteFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
result = 0
while 1:
    shark = biteFish(x, y, size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    nx, ny, dist = shark.pop()

    # 움직이는 칸수가 곧 시간이 된다.
    result += dist
    graph[x][y], graph[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(result)



# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())
# arr = [ list(map(int, input().split())) for _ in range(N)]
#
# fish_list = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] != 0:
#             fish_list.append([arr[i][j], i, j])
#
# fish_list.sort()
#
# # shark 갱신
# shark, si, sj = fish_list[-1]
# shark = 2
# print(shark, si, sj)
# # print(fish_list)
# i = 1
# while True:
#     q = []
#     shark_point = 0
#     for j in range(len(fish_list)):
#         if fish_list[j][0] == i:
#             q.append(fish_list[i])
#     mn = [100000, 0 ,0] # 초기 거리, i, j
#     # 갱신
#     for i in range(len(q)):
#         cal = abs(si-q[i][0]) + abs(sj-q[i][1])
#         if cal < mn[0]:
#             mn[0] = cal
#             mn[1] = q[i][1]
#             mn[2] = q[i][2]
#             q.pop(0)
#             shark_point += 1
#
#         elif cal == mn[0] and q[i][1] < mn[1]:
#             mn[0] = cal
#             mn[1] = q[i][1]
#             mn[2] = q[i][2]
#             q.pop(0)
#             shark_point += 1
#
#     if shark_point == shark:
#         shark += 1
#         shark_point = 0
#         i += 1
#         continue
#
#     print(fish_list)
#     print('q:',q, 'shark_p:', shark_point)
#     print(si, sj)
#     print(mn)
#     break
#
