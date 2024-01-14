n, m, b = map(int, input().split())
ground = [ list(map(int, input().split())) for _ in range(n)]
ans, g_level = float('inf'), 0

for level in range(0, 256 + 1):
    # Step.1 변수 초기화
    # ub 써야 하는 블록, tb 가지고 있는 블록
    ub, tb = 0, 0

    # Step.2 변수 계산
    for i in range(n):
        for j in range(m):

            if ground[i][j] > level:
                tb += ground[i][j] - level

            else:
                ub += level - ground[i][j]

    # Step.3 up가 더 많으면 continue
    if ub > tb + b:
        continue

    # Step.4 ans 갱신
    cnt = tb * 2 + ub
    if cnt <= ans:
        ans = cnt
        g_level = level

print(ans, g_level)