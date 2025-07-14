# 입력
n = int(input())

# 초기값
ans = 0
row = [0] * n

def find(ci):
    for i in range(ci):
        if row[ci] == row[i] or abs(row[ci] - row[i]) == abs(ci - i):
            return False

    return True

def dfs(i):
    global ans
    if i == n:
        ans +=1
        return

    else:
        for j in range(n):
            row[i] = j
            if find(i):
                dfs(i + 1)

dfs(0)
print(ans)

