
t = int(input())

def find(a):
    # print(a, parent[a], ", size:", len(parent))
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def unite(a, b):
    # print("union: ",a,  b)
    ra, rb = find(a), find(b)
    
    # 같으면 return
    if ra == rb: return

    # ra,rb 크기 확인
    if size[ra] < size[rb]:
        ra, rb = rb , ra

    # 갱신
    parent[rb] = parent[ra]
    size[ra] += size[rb]
    return

for _ in range(t):
    n = int(input())
    idx = 0
    friends = {}

    # union find init
    mx = 2 * n + 1
    parent = [i for i in range(mx)]
    size = [1] * mx

    for _ in range(n):
        a, b = input().split()

        # a 추가
        if a not in friends.keys():
            friends[a] = idx
            idx += 1

        if b not in friends.keys():
            friends[b] = idx
            idx += 1

        unite(friends[a], friends[b])
        ans = max(size[friends[a]], size[friends[b]])
        # print(size[1: 20])
        print(size[find(friends[a])])

