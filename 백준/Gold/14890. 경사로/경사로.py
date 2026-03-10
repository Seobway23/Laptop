import sys
input = sys.stdin.readline

# 1. input
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 2. capa():
def capa(line):
    used = [False] * n

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue

        # 높이 차이가 2 이상
        if abs(line[i] - line[i + 1]) > 1:
            return False

        # 오르막: line[i] < line[i+1]
        if line[i] + 1 == line[i + 1]:
            h = line[i]
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != h or used[j]:
                    return False
                used[j] = True

        # 내리막: line[i] > line[i+1]
        elif line[i] - 1 == line[i + 1]:
            h = line[i + 1]
            for j in range(i + 1, i + l + 1):
                if j >= n or line[j] != h or used[j]:
                    return False
                used[j] = True

    return True

# 3. iterator
for i in range(n):
    if capa(arr[i]):   # 행
        cnt += 1

for j in range(n):
    col = [arr[i][j] for i in range(n)]   # 열
    if capa(col):
        cnt += 1


print(cnt)
