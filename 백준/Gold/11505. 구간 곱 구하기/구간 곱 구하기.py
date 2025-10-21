MOD = 1000000007

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        size = 1
        # size 키우기
        while size < self.n:
            size *= 2

        self.size = size
        self.tree = [1] * (2 * size)

        # 리프 채우기
        for i in range(self.n):
            self.tree[size + i] = arr[i] % MOD

        # 바텀업 빌드
        for i in range(size - 1, 0, -1):
            self.tree[i] = (self.tree[i * 2] * self.tree[i * 2 + 1]) % MOD

    def update(self, idx, val):
        p = self.size + idx
        self.tree[p] = val % MOD
        p = p // 2
        while p:
            self.tree[p] = (self.tree[p * 2] * self.tree[p * 2 + 1]) % MOD
            p //= 2

    def query(self, l ,r):
        l += self.size
        r += self.size
        res = 1
        while l <= r:
            if l % 2 == 1:
                res = (res * self.tree[l]) % MOD
                l += 1

            if r % 2 ==0:
                res = (res * self.tree[r]) % MOD
                r -= 1

            l = l // 2
            r = r // 2

        return res

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
st = SegTree(arr)
for _ in range(m + k):
    a, b, c, = map(int, input().split())
    if a == 1:
        st.update(b -1, c)

    else:
        print(st.query(b -1, c - 1))