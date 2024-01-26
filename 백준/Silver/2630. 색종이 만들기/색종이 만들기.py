n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

zero, one = 0, 0


def recur(x, y, n):
    global zero, one

    cur_col = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur_col != arr[i][j]:
                # 분할 호출
                recur(x, y, n//2)
                recur(x, y + n//2, n//2 )
                recur(x + n//2, y, n//2)
                recur(x + n//2, y + n//2, n//2)
                return

    if cur_col == 0:
        zero += 1

    else:
        one += 1


recur(0, 0, n)

print(zero)
print(one)