from collections import deque

n, order = map(int, input().split())
lst = deque(list(i for i in range(1, n + 1)))
ans = []

while True:
    if len(lst) == 1:
        ans.append(lst.popleft())
        break

    for _ in range(order-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())

print("<", str(ans)[1: -1], ">", sep="")