import sys
sys.stdin = open('input.txt')

# x 행, y 열
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 순서
di = [-1,-1,0,1,1,1,0-1]
dj = [0,-1,-1,-1,0,1,1,1]

arr = [list(map(int, input().split())) for _ in range(4)]
k = 1
for i in range(4):
    for j in range(0,8,2):
        # print(k,'번째','물고기:', j, '방향:', j+1)
        k += 1

# shark 처음 위치
arr[0][0] = -1
shark_dir = arr[0][1]

num = 1
while i < 17: # 16까지
    for i in range(4):
        for j in range(0, 8, 2):
            if arr[i][j] == i:
                # 이동 해야 함
                direction = arr[i][j+1]
                ni, nj = i + di[direction*2], j + dj[direction*2]
                print(ni,nj)
                if ni < 0 or ni >= 4 or nj < 0 or nj >= 4 or arr[ni][nj]:
                    while True:
                        direcion = (direction +1) % 8
                        ni, nj = i + di[direction], j + dj[direction]

                        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj]!= -1:
                            break
                # 범위내 일때
                # if 0 <= ni < 4 and 0 <= nj < 4:
                # 둘의 위치 바꾸기
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                arr[i][j+1], arr[ni][nj+1] = arr[ni][nj+1], arr[i][j+1]

print(arr)






'''
상어가 잡을 수 있는 물고기의 최댓값

1. 물고기가 움직인 다음에 상어가 움직임

리스트안의 1부터 15까지 차례대로 이동하는데, 이걸 어떻게 찾지?
어떻게 찾아서 하지? -> 이게 궁금함

@ 물고기의 이동
- 못가는 곳: 상어 or 범위 밖 -> 45도 반시계 회전
- 이동할 때 물고기들이 위치를 이동하는 방식

@ 반복
- 물고기 이동 -> 상어 이동

@ 상어 먹음
- 물고기의 방향을 가지게 됨
- 먹을 수 없으면 집으로감
- 방향의 모든 곳을 먹을 수 있음
- 왠지 dfs가 맞을 것 같음
'''

