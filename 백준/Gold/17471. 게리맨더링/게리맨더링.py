from collections import deque
import sys

input = sys.stdin.readline

# 입력
N = int(input())
people = [0] + list(map(int, input().split()))

# 그래프 양방향 생성
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    for nxt in data[1:]:
        graph[i].append(nxt)
        graph[nxt].append(i)


# group이 연결되어 있는지 확인
def bfs(group):
    visited = [False] * (N + 1)
    q = deque()

    start = next(iter(group))  # group 안의 아무 노드에서 시작
    q.append(start)
    visited[start] = True

    count = 1

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if nxt in group and not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1

    return count == len(group)


answer = float('inf')

# 모든 그룹 분할 경우 확인
for bit in range(1, (1 << N) - 1):
    group1 = set()
    group2 = set()

    for i in range(N):
        if bit & (1 << i):
            group1.add(i + 1)
        else:
            group2.add(i + 1)

    # 두 그룹이 모두 연결되어 있으면 인구 차이 계산
    if bfs(group1) and bfs(group2):
        sum1 = sum(people[x] for x in group1)
        sum2 = sum(people[x] for x in group2)
        answer = min(answer, abs(sum1 - sum2))

print(answer if answer != float('inf') else -1)