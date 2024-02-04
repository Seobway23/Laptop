n, m = map(int, input().split())
lst = list(map(int, input().split()))
prefix_sum, pnt = [], 0
prefix_sum.append(pnt)

for i in range(n):
    pnt += lst[i]
    prefix_sum.append(pnt)

for _ in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])