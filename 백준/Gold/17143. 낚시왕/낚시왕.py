def move(si, sj, speed, dir):
    if dir == 1 or dir == 2:  # 상(1), 하(2) 이동
        if r == 1:
            return si, sj, dir  # 이동할 수 없음
        cycle = 2 * (r - 1)
        s = speed % cycle
        if dir == 1:
            ni = (si - s) % cycle
        else:
            ni = (si + s) % cycle
        if ni >= r:
            ni = cycle - ni
            dir = 3 - dir  # 방향 전환 (1 <-> 2)
        return ni, sj, dir
    else:  # 우(3), 좌(4) 이동
        if c == 1:
            return si, sj, dir  # 이동할 수 없음
        cycle = 2 * (c - 1)
        s = speed % cycle
        if dir == 4:
            nj = (sj - s) % cycle
        else:
            nj = (sj + s) % cycle
        if nj >= c:
            nj = cycle - nj
            dir = 7 - dir  # 방향 전환 (3 <-> 4)
        return si, nj, dir

# init
r, c, m = map(int, input().split())
sharks = dict()
ans = 0
di, dj =  [-1, 0, 1, 0], [0, 1, 0, -1] # 0 상, 1 우, 2 하, 3 좌

for _ in range(m): # i, j  -1 씩 해줘야 함, 딕셔너리 저장 -> 시간초과 방지
    i, j, s, d, z = map(int, input().split())
    i -= 1    # i
    j -= 1    # j
    sharks[(i, j )] = [s, d, z]     # dict에 shark 추가

# main loop
for j in range(c):
    # Fishing
    targets = [pos  for pos in sharks if pos[1] == j]
    if targets:
        target = min(targets, key=lambda x: x[0])
        # [0]: speed, [1]: direction, [2]: size
        ans  += sharks[target][2]
        del sharks[target]

    # Move
    new_sharks = dict()
    for (i, j), (s, d, z) in sharks.items():
        ni, nj, nd = move(i, j , s, d)

        key = (ni, nj)
        # 겹치면, size가 크면 추가
        if key in new_sharks:
            if new_sharks[key][2] < z:
                new_sharks[key] = [s, nd, z]

        # 안겹치면 추가
        else:
            new_sharks[key] = [s, nd, z]

    # sharks 갱신
    sharks = new_sharks

print(ans)