def z(n, r, c):
    if n == 0:
        return 0

    # n부터 크기가 큰대로 size 누적
    size = 2 ** ( n - 1)

    # 1 첫번째
    if r < size and c < size:
        return z(n -1, r, c)

    # 2 두번째
    elif r < size <= c:
        return size * size + z(n-1, r, c - size)

    # 3 세번째
    elif r >= size > c:
        return 2 * size * size + z(n - 1, r - size, c)

    else: # 4번째
        return 3 * size * size + z(n-1, r - size, c - size)


n, r, c = map(int, input().split())
print(z(n, r, c))