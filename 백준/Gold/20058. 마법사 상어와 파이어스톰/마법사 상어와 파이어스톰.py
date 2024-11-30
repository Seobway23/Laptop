
from collections import deque

N, Q = map(int, input().split())
n =  2 ** N # 전체 크기
arr = [list(map(int, input().split())) for _ in range(n)]
L_list = list(map(int, input().split()))

# q만큼 순회
for L in L_list:
    l = 2 ** L  # 격자 크기
    new_arr = [[0] * n for _ in range(n)]

    for i in range(0, n, l):    # l 간격 만큼 순회
        for j in range(0, n, l):
            # L 격자 회전
            for di in range(l):
                for dj in range(l):
                    ci, cj = i + di, j + dj
                    ri, rj = i + dj, j + (l -1) - di # l 은 격자 크기
                    # 바꾸기
                    new_arr[ri][rj] = arr[ci][cj]


    # 얼음 -1 하기
    # 동시에 일어 나기 때문에 복사 배열을 써야 한다
    # 동시에 일어나는 작업은 slicing 으로 해야 한다 -> deepcopy 보다 속도 빠름
    ice_arr = [row[:] for row in new_arr]
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] > 0:
                cnt = 0
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < n and new_arr[ni][nj] > 0:
                        cnt += 1

                # 인접 얼음이 3개 미만 이라면
                if cnt < 3:
                    ice_arr[i][j] -= 1

    # 마지막 arr 갱신
    arr = ice_arr

# 남아 있는 얼음의 합 구하기
sm = sum(map(sum, arr))
print(sm)

# 남아 있는 가장 큰 덩어리 칸의 갯수
visited =[[0] * n for _ in range(n)]
ans = 0
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            q.append((i, j))
            visited[i][j] = 1
            cnt2 = 1
            # 시 작
            while q:
                ci, cj = q.popleft()

                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = ci + di, cj + dj

                    # 범위내, 얼음 > 0, 미방문
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > 0 and visited[ni][nj]==0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        cnt2 += 1


            ans = max(ans, cnt2)

print(ans)