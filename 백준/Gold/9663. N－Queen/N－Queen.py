# 입력
n = int(input())

def dfs(i):
    global ans
    # 종료 조건
    if i == n:
        ans += 1
        return

    # 가로 X, 대각선 아래 X, 대각선 위 X
    for j in range(n):
        if v1[j] == v2[i + j] == v3[i - j] == 0:
            v1[j] = v2[i + j] = v3[i - j] = 1
            dfs(i + 1)
            v1[j] = v2[i + j] = v3[i - j] = 0


# init
ans = 0
v1 = [0]* n # 가로
v2 = [0] * (2*n) # 대각선 위
v3 = [0] * (2 * n) # 대각선 아래
dfs(0)
print(ans)