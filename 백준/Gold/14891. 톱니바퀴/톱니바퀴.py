from collections import deque


def check_right(g, direction):
    global Dir
    if g > 3 or gear[g-1][2] == gear[g][6]:
        return

    if gear[g-1][2] != gear[g][6]:
        # 돌릴 때 움직이려면 방향이 반대여야 함
        check_right(g + 1, -direction)
        # 돌린다음에 체크
        gear[g].rotate(direction)

def check_left(g, direction):
    global Dir
    if g < 0 or gear[g][2] == gear[g+1][6]:
        return

    if gear[g][2] != gear[g+1][6]:
        check_left(g - 1, -direction)
        gear[g].rotate(direction)


gear = [deque(list(map(int, input()))) for _ in range(4)]
N = int(input())

# dir 체크
for _ in range(N):
    G, direction = map(int, input().split())
    g = G-1
    check_right(g+1, -direction)
    check_left(g-1, -direction)
    # 돌린다음에 체크하면 안되니까 돌리기전에 체크, 그리고 마지막에 돌리기
    gear[g].rotate(direction)

ans = 0
for i in range(4):
    # print(gear[i])
    if gear[i][0] == 1:
        ans += 2**i
print(ans)