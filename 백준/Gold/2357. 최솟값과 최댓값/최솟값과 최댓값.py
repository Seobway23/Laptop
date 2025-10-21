INF = 10**9 + 1

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        size = 1
        # size 키우기
        while size < self.n:
            size *= 2

        self.size = size
        self.tree = [(INF, -INF)] * (2 * size)

        # 리프 채우기
        for i in range(self.n):
            v = arr[i]
            self.tree[size + i] = (v, v)

        # 바텀업 빌드
        for i in range(size - 1, 0, -1):
            lmin, lmax = self.tree[i * 2]
            rmin, rmax = self.tree[i * 2 + 1]
            self.tree[i] = (min(lmin, rmin), max(lmax, rmax))

    def query(self, l ,r):
        l += self.size
        r += self.size
        mn, mx = 1000000000, 0

        while l <= r:
            if l % 2 == 1:
                mn = min(mn, self.tree[l][0])
                mx = max(mx, self.tree[l][1])
                l += 1
            if r % 2 == 0:
                mn = min(mn, self.tree[r][0])
                mx = max(mx, self.tree[r][1])
                r -= 1
            l //= 2
            r //= 2

        return mn, mx

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
st = SegTree(arr)
for _ in range(m):
    a, b, = map(int, input().split())
    print(*st.query(a -1, b - 1))