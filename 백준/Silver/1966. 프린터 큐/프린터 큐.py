from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        best = max(q)
        front = q.popleft()
        m -= 1  # 위치 상대 계산

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else:
            q.append(front)
            if m < 0:
                m = len(q) -1

