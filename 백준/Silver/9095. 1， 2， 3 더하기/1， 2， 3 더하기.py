def dfs(num, target):
    global ans

    if num < target:
        return

    if num == target:
        ans += 1
        return

    # + 1
    dfs(num, target + 1)
    # + 2
    dfs(num, target + 2)
    # + 3
    dfs(num, target + 3)
    return


n = int(input())
for _ in range(n):
    ans = 0
    num = int(input())
    dfs(num, 0)
    print(ans)
