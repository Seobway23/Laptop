from collections import deque

n = int(input())
apple_nums = int(input())

apples = set()
for _ in range(apple_nums):
    ai, aj = map(int, input().split())
    # 사과 처리
    apples.add((ai-1, aj-1))

cmd_nums = int(input())
cmd = dict()
for _ in range(cmd_nums):
    X, C = input().split()
    cmd[int(X)] = C


# 동 남 서 북
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0
time, ni, nj = 0, 0, 0

# snake 위치
snake = deque()
snake.append((ni,nj))

while True:
    time += 1
    # 다음 위치
    ni, nj = ni + di[direction], nj + dj[direction]

    # 범위 벗어남 종료
    if not (0 <= ni < n and 0 <= nj < n):
        break

    # 자기 자신과 쾅하면 종료
    if (ni, nj) in snake:
        break

    # snake 위치 이동
    snake.appendleft((ni, nj))

    if (ni, nj) in apples:
        # 사과 먹으면 머리 이동
        apples.remove((ni, nj))
    else:
        # 사과를 못 먹으면 꼬리 이동
        snake.pop()

    # 방향 전환
    if time in cmd:
        if cmd[time] == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)


