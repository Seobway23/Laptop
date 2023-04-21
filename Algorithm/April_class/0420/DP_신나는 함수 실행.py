# import sys
# sys.stdin = open('input.txt', 'r')


def func(N):
    if N == 1:
        return 1

    elif N == 2:
        return 2

    v[1] = 1
    v[2] = 2
    for i in range(3, N + 1):
        v[i] = v[i - 1] + v[i - 2]
        v[i] %= 15746

    return v[N]


N = int(input())
v = [0] * ( N + 1)
print(func(N))