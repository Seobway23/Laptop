from copy import deepcopy

# init
n, m, k = map(int, input().split())
dir = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j, m, s, d = map(int, input().split())
    arr[i-1][j-1].append((m, s, d))

for _ in range(k):
    # move
    # pprint(arr)

    # 1 step
    next_arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]: # fireball, it is
                for k in range(len(arr[i][j])):
                    # [0]: 질량, [1]: 방향, [2]: 속력
                    m, s, d = arr[i][j][k]
                    ni, nj = (i + dir[d][0] * s) % n, (j + dir[d][1] * s) % n
                    next_arr[ni][nj].append((m, s, d))
    # 만약 겹치면
    for i in range(n):
        for j in range(n):
            if len(next_arr[i][j]) > 1:
                # pop 하고 [] 갱신
                targets = next_arr[i][j]
                next_arr[i][j] = []

                new_m = sum(row[0] for row in targets) // 5
                # 질량 // 5 > 0
                if new_m > 0:
                    new_s = sum(row[1] for row in targets) // len(targets)

                    # 방향 설정
                    one, two = 0, 0 # 홀, 짝
                    for target in targets:
                        if target[2] % 2 == 1: # 홀수라면?
                            one += 1
                        else: two += 1

                    if len(targets) == one or len(targets) == two:
                        # 0, 2, 4, 6 설정
                        for k in (0, 2, 4, 6): # 나뉘지만, 움직이지 않음
                            next_arr[i][j].append((new_m, new_s, k))


                    else:
                        for k in (1, 3, 5, 7): # 나뉘지만, 움직이지 않음
                            next_arr[i][j].append((new_m, new_s, k))

    # pprint(next_arr)
    # 갱신
    arr = next_arr

# 남아있는 합계
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            for k in range(len(arr[i][j])):
                ans += arr[i][j][k][0]

print(ans)