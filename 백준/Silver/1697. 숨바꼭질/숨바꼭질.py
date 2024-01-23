from collections import deque

n, k = map(int, input().split())

ans = 100000
q = deque()
q.append([n, 0])
visited = set()

while q:
    t, cnt = q.popleft()

    # 동생의 위치에 도달한 경우
    if t == k:
        ans = min(ans, cnt)
        break

    # 방문한 위치는 무시
    if t in visited:
        continue
    visited.add(t)

    # 다음 위치 탐색
    for next_t in [t + 1, t - 1, t * 2]:
        if 0 <= next_t <= 100000:  # 유효한 범위 내에서만 탐색
            q.append([next_t, cnt + 1])

print(ans)