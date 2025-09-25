n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arrive = list(map(int, input().split()))
parent = [i for i in range(n)]
size =  [0] * n

def find(x):
    # 처음에 똑같은 루트 만나면 갱신
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def unite(a, b):
    ra, rb = find(a), find(b)

    # 길이 크기 비교
    if size[rb] > size[ra]:
        ra, rb = rb, ra

    parent[rb] = parent[ra] # 부모 갱신
    size[ra] += size[rb] # size 갱신,

    return


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            unite(i, j)


diff = find(arrive[0] - 1)
ans = "YES"
for i in arrive:
    i -= 1  # 0 base 에 맞춰야 함
    if find(i) != diff:
        ans = "NO"
        break

print(ans)
