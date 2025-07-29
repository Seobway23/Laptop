n, m = map(int, input().split())
dist = [[float('inf')] * n for _ in range(n)]
next_hop = [[-1] * n for _ in range(n)]


# i == j 일 때 0 넣기
for i in range(n):
    dist[i][i] = 0

# 입력
for _ in range(m):
    s, e, val = map(int, input().split())
    s, e, = s - 1, e - 1
    # 중복 간선의 경우, 더 작은 가중치 남기기
    if val < dist[s][e]:
        dist[s][e], dist[e][s] = val, val
        next_hop[s][e], next_hop[e][s] = e, s

# Floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            new_dist = dist[i][k] + dist[k][j]
            if dist[i][j] > new_dist:
                dist[i][j] = new_dist
                # 마지막 i -> k 저장
                next_hop[i][j] = next_hop[i][k]


# 입력
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append('-')
        else:
            # next_hop 에 저장된 0-based 값을 1-based로 변환
            row.append(str(next_hop[i][j] + 1))
    # join 은 각 원소 사이에만 공백을 넣고, 맨 앞/뒤는 공백이 없습니다
    print(' '.join(row))
