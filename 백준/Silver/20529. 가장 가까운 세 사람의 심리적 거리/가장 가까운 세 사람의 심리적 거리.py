n = int(input())
for _ in range(n):
    t = int(input())
    lst = list(input().split())
    ans = float('inf')

    if t > 32:
        print(0)
        continue

    for i in range(t-2):
        for j in range(i+1, t-1):
            for k in range(j + 1, t):
                cnt = 0
                a, b, c = lst[i], lst[j], lst[k]

                for d in range(4):
                    if a[d] != b[d]: cnt += 1
                    if a[d] != c[d]: cnt += 1
                    if b[d] != c[d]: cnt += 1

                ans = min(cnt, ans)

    print(ans)
