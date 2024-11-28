import sys
input = sys.stdin.readline

def move(si, sj, speed, dir):
    if dir == 0 or dir == 2:  # Up or Down
        cycle = (r - 1) * 2
        if cycle != 0:
            speed %= cycle
        else:
            speed = 0
        for _ in range(speed):
            if si == 0 and dir == 0:
                dir = 2
            elif si == r - 1 and dir == 2:
                dir = 0
            si += di[dir]
    else:  # Left or Right
        cycle = (c - 1) * 2
        if cycle != 0:
            speed %= cycle
        else:
            speed = 0
        for _ in range(speed):
            if sj == 0 and dir == 3:
                dir = 1
            elif sj == c - 1 and dir == 1:
                dir = 3
            sj += dj[dir]
    return si, sj, dir

r, c, m = map(int, input().split())
sharks = dict()
direction_map = {1: 0, 2: 2, 3: 1, 4: 3}
di = [-1, 0, 1, 0]  # Up, Right, Down, Left
dj = [0, 1, 0, -1]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    d = direction_map[d]
    sharks[(x, y)] = [s, d, z]

ans = 0

for j in range(c):
    # Fishing
    candidates = [pos for pos in sharks if pos[1] == j]
    if candidates:
        target = min(candidates, key=lambda x: x[0])
        ans += sharks[target][2]
        del sharks[target]
    # Move sharks
    new_sharks = dict()
    for (x, y), (s, d, z) in sharks.items():
        nx, ny, nd = move(x, y, s, d)
        key = (nx, ny)
        if key in new_sharks:
            if new_sharks[key][2] < z:
                new_sharks[key] = [s, nd, z]
        else:
            new_sharks[key] = [s, nd, z]
    sharks = new_sharks

print(ans)
