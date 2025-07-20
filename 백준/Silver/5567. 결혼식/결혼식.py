from collections import deque

n = int(input())
m = int(input())
arr = [[0] * n for _ in range(n)]
v = [0]

for _ in range(m):
    n1, n2 = map(int, input().split())
    arr[n1-1][n2-1] , arr[n2-1][n1-1] = 1, 1

q = deque([0])
for _ in range(2):
    for _ in range(len(q)):
        ci = q.popleft()
        for j in range(n):
            if  arr[ci][j] == 1:
                q.append(j)
                v.append(j)

print(len(set(v)) - 1)