#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 MOD = 1'000'000'007;

int N, M, K;
vector<int64> arr, seg; // seg size: 4*N

int64 build(int node, int l, int r) {
    if (l == r) return seg[node] = arr[l] % MOD;
    int mid = (l + r) / 2;
    int left = node * 2, right = left + 1;
    int64 a = build(left, l, mid);
    int64 b = build(right, mid + 1, r);
    return seg[node] = (a * b) % MOD;
}

int64 query(int node, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 1;               // 곱의 항등원
    if (ql <= l && r <= qr) return seg[node];
    int mid = (l + r) / 2;
    int left = node * 2, right = left + 1;
    int64 a = query(left, l, mid, ql, qr);
    int64 b = query(right, mid + 1, r, ql, qr);
    return (a * b) % MOD;
}

void update(int node, int l, int r, int idx, int64 val) {
    if (l == r) {
        seg[node] = val % MOD;
        return;
    }
    int mid = (l + r) / 2;
    if (idx <= mid) update(node*2, l, mid, idx, val);
    else            update(node*2+1, mid+1, r, idx, val);
    seg[node] = (seg[node*2] * seg[node*2+1]) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;
    arr.resize(N);
    for (int i = 0; i < N; ++i) cin >> arr[i];

    seg.assign(4 * N, 1);
    build(1, 0, N - 1);

    int a; int b; long long c;
    for (int i = 0; i < M + K; ++i) {
        cin >> a >> b >> c;
        if (a == 1) {
            update(1, 0, N - 1, b - 1, c);
        } else {
            cout << query(1, 0, N - 1, b - 1, c - 1) << '\n';
        }
    }
    return 0;
}
