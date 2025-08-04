n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
counts = {-1 : 0, 0: 0, 1: 0}

def dfs(x, y, size):
    first_value  = arr[x][y]

    # 같은 값인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first_value: # 같지 않다면
                new_size = size // 3

                for dx in range(3):
                    for dy in range(3):
                        dfs(x + dx * new_size, y + dy * new_size, new_size)

                return

    # 모두 같다면 셈( size = 1 포함)
    counts[first_value] += 1


dfs(0, 0, n)
print(counts[-1])
print(counts[0])
print(counts[1])