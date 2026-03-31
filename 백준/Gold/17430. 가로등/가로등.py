t = int(input())

for _ in range(t):
    n = int(input())
    xs = set()
    ys = set()

    for _ in range(n):
        x, y = map(int, input().split())
        xs.add(x)
        ys.add(y)

    if len(xs) * len(ys) == n:
        print("BALANCED")
    else:
        print("NOT BALANCED")