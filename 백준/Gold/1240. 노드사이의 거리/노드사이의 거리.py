from collections import deque

def bfs(start, end):
    q = deque()
    v = [0] * n
    cnt = 0
    # 초기 값 추가
    q.append((start, cnt))
    v[start] = 1

    while q:
        ti, tcnt = q.popleft()

        # 종료 조건
        if ti == end:
            return tcnt

        for j in range(n):
            if arr[ti][j] and not v[j]:
                # q 추가, 방문 추가
                q.append((j, tcnt + arr[ti][j]))
                v[j] = 1

    return 1


n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for _ in range(n - 1):
    n1, n2, value = map(int, input().split())
    arr[n1 - 1][n2 - 1],arr[n2 - 1][n1 - 1] = value, value # 동시 할당


for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s - 1, e - 1))