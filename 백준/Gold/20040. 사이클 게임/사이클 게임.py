n, m = map(int, input().split())
p, s = [i for i in range(n)], [1] * n

def unite(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return

    # 갱신
    if s[rb] > s[ra]:
        ra, rb = rb, ra

    # 사이즈, 크기 갱신
    s[ra] += s[rb]
    p[rb] = p[ra]
    return

def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

ans = 0

for time in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        ans = time
        break
    unite(a, b)

print(ans)