class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node, l, r):
        if l == r:
            # 리프 노드
            self.tree[node] = self.arr[l]
            return

        # 중간 인덱스 =
        mid = (l + r) // 2

        # 왼쪽 자식
        self._build(node * 2, l , mid)
        # 오른쪽 자식
        self._build(node * 2 + 1, mid + 1, r)
        # 현재 노드 값 = 왼쪽 + 오른 쪽
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]


    def query(self, ql, qr):
        # 외부에서 구간[ql, qr]의 합을 알 고 싶을 때, 호출
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        # node: 현재 노드
        # [l, r] : 노드가 담당하는 구간
        # [ql, qr]: 우리가 구하고 싶은 구간
        if qr < l or r < ql:
            # 범위가 겹치지 않으면 0
            return 0

        if ql <= l and r <= qr:
            # 완전히 포함되면 현재 노드 값 반환
            return self.tree[node]

        # 일부만 겹친다면
        mid = (l + r) // 2
        left_sum = self._query(node * 2, l , mid, ql, qr)
        right_sum = self._query(node * 2+ 1, mid + 1, r, ql, qr)
        return left_sum + right_sum

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, l, r, idx, val):
        # node: 현재 노드
        # [l, r]: 이 노드가 담당하는 구간
        # idx: 바꿀 원소 인덱스

        if l == r:
            # 리프 노드
            self.tree[node] = val
            return

        mid = (l + r) // 2
        if idx <= mid:
            # 업데이트할 인덱스가 왼쪽 구간에 있으면 왼쪽 자식으로 이동
            self._update(node * 2, l, mid, idx, val)
        else:
            # 오른쪽 구간에 있으면 오른쪽 자식으로 이동
            self._update(node * 2 + 1, mid + 1, r, idx, val)

        # 자식들의 합 다시 갱신
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]


arr = [2, 1, 3, 5, 4]
st = SegmentTree(arr)

n, m, k = map(int ,input().split())
arr = [int(input()) for _ in range(n)]
st = SegmentTree(arr)
for _ in range(k + m):
    a, b, c = map(int, input().split())
    if a == 1:
        # b 번째수를 c로 바꾸기 -> b - 1
        st.update(b - 1, c)

    else:
        print(st.query(b - 1, c - 1))
