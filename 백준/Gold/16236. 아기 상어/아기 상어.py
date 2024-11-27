
from collections import deque

def BFS(si, sj):
    # init
    q = deque()
    v = [[0] * n for _ in range(n)]

    # 한 스텝 추가를 어떻게 하지 ?
    tlst = []
    cnt = 0

    # q추가
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ti, tj = q.popleft()
        if v[ti][tj] == cnt:
            return tlst, cnt  - 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ti + di, tj + dj

            # 범위내, 미방문, 조건 내
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and shark >= arr[ni][nj]:
                # q 추가
                q.append((ni, nj))

                # 방문 표시
                v[ni][nj] = v[ti][tj] + 1

                # 물고기 eat
                if shark > arr[ni][nj] > 0:
                    tlst.append((ni, nj))
                    cnt = v[ni][nj]


    # 첫 방문을 1로 잡았으니까 나머지에서 1 빼줘야 함
    return tlst, cnt - 1

# init
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
shark = 2
eat = 0

# shark 위치
si, sj =  0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0

# main loop
while True:
    tlst, cnt = BFS(si, sj)
    # si, sj 갱신

    # shark 이동이 없다면 => 이거 어떻게 풀이 하는지 나중에 봐야 함
    if len(tlst) == 0:
        break

    # i, j 순 정렬
    tlst.sort(key = lambda x: (x[0], x[1]))
    si, sj = tlst[0]

    # 물고기 위치 0 갱신
    arr[si][sj] = 0
    eat += 1

    # eat , shark 갱신
    if shark == eat:
        shark += 1
        eat = 0


    # ans 갱신
    ans += cnt


print(ans)
