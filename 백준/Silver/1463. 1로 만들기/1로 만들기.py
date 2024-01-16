def dfs(target, ans_tar):
    global ans, n
    if target == 1:
        if ans > ans_tar:
            ans = ans_tar
        return
    
    if ans < ans_tar:
        return

    if target % 3 == 0:
        dfs(target // 3, ans_tar + 1)

    if target % 2 == 0:
        dfs(target // 2, ans_tar + 1)

    dfs(target - 1, ans_tar + 1)

n = int(input())
ans = 10**6

target = n
dfs(target, 0)

print(ans)