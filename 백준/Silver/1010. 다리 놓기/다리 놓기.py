t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # mCn
    ans = 1
    for i in range(m - n + 1, m+1):
        ans *= i
        # print(i)

    for j in range(1, n+1):
        ans = int(ans // j)
        # print(j, "j")

    print(ans)