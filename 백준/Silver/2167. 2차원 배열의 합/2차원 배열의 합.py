n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


t = int(input())
for _ in range(t):
    ans = 0
    i, j, x, y = map(int, input().split())
    for ci in range(i-1, x):
        for cj in range(j-1, y):
            ans += arr[ci][cj]

    print(ans)