from collections import deque
n = int(input())

ans = deque()

for _ in range(n):
    num = int(input())

    if num == 0:
        ans.pop()

    else:
        ans.append(num)

# 정답 처리
cnt = 0
for i in ans:
    cnt += i

print(cnt)
