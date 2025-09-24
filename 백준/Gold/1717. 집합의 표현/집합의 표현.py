n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

def find(x):
    # 대표자를 찾아가면서 올라감
    if parent[x] != x:
        parent[x] = find(parent[x])

    # print("파인드: ", x, parent[x])
    return parent[x]

def union(a, b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    # parent, size 갱신
    parent[root_b] = parent[root_a]
    size[root_a] += size[root_b]
    # print("파인드:", (root_a, root_b), ", size:", (size[root_a], size[root_b]))


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)

    else:
        print("YES" if find(a) == find(b) else "NO")
