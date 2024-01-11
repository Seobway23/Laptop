t = int(input())
lst = [0] * (10000 + 1)

for _ in range(t):
    lst[int(input())] += 1

for i in range(1, 10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i)