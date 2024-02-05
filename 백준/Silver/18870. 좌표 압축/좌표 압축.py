n = int(input())
lst = list(map(int, input().split()))
n_lst = sorted(set(lst))
dic = {n_lst[i]: i for i in range(len(n_lst))}

for i in lst:
    print(dic[i], end=" ")