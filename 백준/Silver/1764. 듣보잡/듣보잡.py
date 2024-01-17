n, m = map(int, input().split())
people_lst = dict()

for _ in range(n):
    people = input()
    people_lst[people] = 0
    people_lst[people] += 1

for _ in range(m):
    people = input()
    if people in people_lst.keys():
        people_lst[people] += 1

    else:
        people_lst[people] = 1


ans = []
for i in people_lst:
    if people_lst[i] >= 2:
        ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
    print(i)