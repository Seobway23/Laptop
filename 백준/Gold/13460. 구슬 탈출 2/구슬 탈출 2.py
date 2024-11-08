from collections import deque

# 입력 받기
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 상하좌우 방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 방문 기록 및 큐
v = []  # 방문 리스트
q = deque()  # BFS 큐
cnt = 1  # 초기 이동 횟수

# 초기값 지정
def init():
    global q, v
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':  # 빨간 구슬 위치
                ri, rj = i, j
            elif arr[i][j] == 'B':  # 파란 구슬 위치
                bi, bj = i, j
    # 초기 상태 추가
    v.append((ri, rj, bi, bj))
    q.append((ri, rj, bi, bj, cnt))

# 공 이동 함수
def road_search(i, j, di, dj):
    road = 0
    # 벽(#)에 막히거나 구멍(O)에 빠질 때까지 이동
    while arr[i + di][j + dj] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        road += 1
    return i, j, road

# BFS 함수
def BFS():
    init()
    while q:
        ri, rj, bi, bj, cnt = q.popleft()

        # 종료 조건: 10번 초과
        if cnt > 10:
            break

        # 4방향 탐색
        for k in range(4):
            # 빨간 구슬 이동
            rni, rnj, r_count = road_search(ri, rj, di[k], dj[k])
            # 파란 구슬 이동
            bni, bnj, b_count = road_search(bi, bj, di[k], dj[k])

            # 파란 구슬이 구멍에 빠지면 실패
            if arr[bni][bnj] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if arr[rni][rnj] == 'O':
                return cnt

            # 두 구슬이 같은 위치에 있으면 충돌 처리
            if rni == bni and rnj == bnj:
                if r_count > b_count:  # 빨간 구슬이 더 멀리 이동
                    rni -= di[k]
                    rnj -= dj[k]
                else:  # 파란 구슬이 더 멀리 이동
                    bni -= di[k]
                    bnj -= dj[k]

            # 새로운 상태가 방문되지 않았다면 추가
            if (rni, rnj, bni, bnj) not in v:
                v.append((rni, rnj, bni, bnj))
                q.append((rni, rnj, bni, bnj, cnt + 1))

    # 실패 시 -1 반환
    return -1

print(BFS())
