from collections import deque

def dfs(start):
    v = [0] * n
    q = deque([start])
    v[start] = 1
    cnt = 0

    while q:
        t = q.popleft()
        for i in arr[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
# 배열 n X n 은 절대 될 수 없음, 4byte 라 쳐도 250MB 그냥 넘어감
arr = [[] for _ in range(n)]

for _ in range(m):
    e, s = map(int, input().split())
    arr[s-1].append(e-1)

ans = []
# cnt
for j in range(n):
    value = dfs(j)
    ans.append((j, value))

ans.sort(key=lambda x : (-x[1], x[0]))
print_ans = list(row[0] + 1 for row in ans if row[1] == ans[0][1])
print(*print_ans)