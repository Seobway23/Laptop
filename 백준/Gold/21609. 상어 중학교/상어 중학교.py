from collections import deque

def block_select():
    block_lst = []
    q = deque()

    for i in range(n):
        for j in range(n):
            rainbow_blocks = []
            d= arr[i][j] != -1 ; dd = arr[i][j] ; ddd = visited[i][j]
            if arr[i][j] not in spear and arr[i][j] != 0 and visited[i][j] == 0:   # 검은, 무지개가 아닐 때
                # not arr 와 arr != 0 은 다르다!
                # q 추가, 방문 표시
                q.append((i, j))
                visited[i][j] = 1
                lst = [(i, j, arr[i][j])]
                rainbow_blocks = []

                # BFS 돌기
                while q:
                    ti, tj = q.popleft()

                    # 4방향 탐색
                    for di, dj in dir:
                        ni, nj = ti + di, tj + dj
                        # 범위내 and (해당 색 or 무지개 색) and 미방문
                        if (0 <= ni < n and 0 <= nj < n) and (arr[ni][nj] == arr[i][j] or arr[ni][nj] == 0) and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            q.append((ni, nj))
                            # [2]: 블록 추가
                            num = 0 if arr[ni][nj] == 0 else 1
                            lst.append((ni, nj, num))
                            if arr[ni][nj] == 0:
                                rainbow_blocks.append((ni, nj))

                # 무지개 블록 방문 해제
                for ni, nj in rainbow_blocks:
                    visited[ni][nj] = 0

                lst.sort(key = lambda x: (
                        x[0] if x[2] != 0 else float('inf'),  # x[0]: x[2] != 0일 때만, 그렇지 않으면 큰 값
                         x[1] if x[2] != 0 else float('inf'))  # x[1]: x[2] != 0일 때만
                    )
                # print(lst)
                block_lst.append(lst)

    # 기준 블록 선정 & one block 선정
    block_lst.sort(key= lambda x: (-len(x), -sum(1 for item in x if item[2] == 0), -x[0][0] , -x[0][1]))
    if block_lst and len(block_lst[0]) > 1:
        return block_lst[0]
    return

def gravity():
    for j in range(n):
        # 가지 치기
        if 99 in list(zip(*arr))[j]:
            for i in range(n-1, -1, -1):
                if arr[i][j] not in spear: # 구슬 이라면 확인
                    gq = deque()
                    gq.append((i, j ))
                    while gq:
                        ti, tj = gq.popleft()
                        ni, nj = ti + 1, tj
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 99:
                            gq.append((ni, nj))

                        if not gq:
                            arr[ti][tj], arr[i][j] = arr[i][j], arr[ti][tj]
                            break
    return

def rotate():
    rotate_arr = [row[:] for row in arr]
    for i in range(n):
        for j in range(n):
            rotate_arr[n-1 - j][i] = arr[i][j]

    return rotate_arr

# 구슬이 아닌 리스트
spear = [-1, 99]

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
    visited = [[0] * n for _ in range(n)]
    # 1. 블록 선택
    block = block_select()

    # 종료 조건
    if not block:
        break

    # 2-1. 블록 제거 / 99 는 블록 제거
    for i, j, _ in block:
        arr[i][j] = 99

    # 2-1. ans 갱신
    ans += len(block) ** 2

    # 중력 작용
    gravity()
    # print("전:", arr)

    # rotate
    arr = rotate()
    # print("후:", arr)

    # 다시 중력 작용
    gravity()
    # print("중:", arr)

print(ans)