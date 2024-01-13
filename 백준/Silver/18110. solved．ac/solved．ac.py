def Round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input())
if n == 0:
    print(0)

else:
    lst = list(int(input()) for _ in range(n))
    lst.sort()
    b = Round(n * 0.15)
    trim_lst = lst[b:-b] if b > 0 else lst
    print(Round(sum(trim_lst) / len(trim_lst)))