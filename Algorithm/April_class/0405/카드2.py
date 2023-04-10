from collections import deque

T = int(input())

arr = [i for i in range(1, T+1)]
lst = deque()
lst += arr
print(lst)
while len(lst) > 1:
    lst.popleft()
    t = lst.popleft()
    lst.append(t)
    print('lst:', lst, 't:', t)
print(*lst)


# a.insert(인덱스, 넣을 꺼)