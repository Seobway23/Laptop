MOD = 1000000007

class SegTree():
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node, l, r):
        if l == r:
            self.tree[node] = self.arr[l]
            return

        mid = (l + r) // 2
        self._build(node * 2, l, mid)
        self._build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.tree[node * 2] * self.tree[node * 2 + 1] % MOD

    def query(self, ql, qr):
        if ql > qr: return 1
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        # 범위 밖
        if ql > r or qr < l:
            return 1

        # 범위 내
        if ql <= l and r <= qr:
            return self.tree[node]

        # 일부 포함 이라면
        mid = (r + l) // 2
        left_sum = self._query(2 * node, l, mid, ql, qr)
        right_sum = self._query(2 * node + 1, mid +1, r, ql, qr)
        return left_sum * right_sum % MOD



    def update(self, idx, val):
        return self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, l , r, idx, val):
        if l == r:
            self.tree[node] = val
            return

        # 찾아가기
        mid = (l  + r ) // 2
        if  idx <= mid:
            self._update(node * 2, l, mid, idx, val)

        else:
            self._update(node * 2 + 1, mid + 1, r , idx, val)


        # 트리 갱신
        self.tree[node] = self.tree[node * 2] * self.tree[node * 2 + 1] % MOD


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
st = SegTree(arr)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        st.update(b -1, c)
    else:
        print(st.query(b - 1, c - 1))
