#include <bits/stdc++.h>
using namespace std;

struct SegTree {
    int n;                       // 전체 배열 길이
    vector<long long> seg;       // 세그먼트 트리(합 저장)
    vector<long long> lazy;      // lazy 가산값

    // 생성자: 트리/레이지 배열 크기 할당
    SegTree(int n) : n(n), seg(4 * n, 0), lazy(4 * n, 0) {}

    // 내부 build: idx 노드가 [l,r] 구간 담당, a는 1-indexed 배열
    void build(const vector<long long>& a, int idx, int l, int r) {
        if (l == r) {
            // 리프: 해당 위치 값 그대로 저장
            seg[idx] = a[l];
            return;
        }
        int mid = (l + r) >> 1;
        // 왼쪽 자식: idx<<1, [l,mid]
        // 오른쪽 자식: idx<<1|1, [mid+1,r]
        build(a, idx << 1, l, mid);
        build(a, idx << 1 | 1, mid + 1, r);
        // 부모 합 = 왼 + 오
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1];
    }

    // lazy 전파: 현재 idx의 lazy를 두 자식에게 내림
    // 호출 시점: 부분 겹침으로 자식으로 내려가야 할 때만
    void push(int idx, int l, int r) {
        if (lazy[idx] == 0) return; // 밀린 게 없으면 종료
        long long v = lazy[idx];    // 밀린 가산값
        int mid = (l + r) >> 1;

        // 왼쪽 자식에게 전파
        // 왼쪽 자식 구간 길이: (mid - l + 1)
        seg[idx << 1]      += v * (mid - l + 1);
        lazy[idx << 1]     += v;

        // 오른쪽 자식에게 전파
        // 오른쪽 자식 구간 길이: (r - mid)
        seg[idx << 1 | 1]  += v * (r - mid);
        lazy[idx << 1 | 1] += v;

        // 현재 노드의 lazy는 전파 완료했으므로 0으로 초기화
        lazy[idx] = 0;
    }

    // 구간 [ql, qr]에 val 더하기
    void range_add(int idx, int l, int r, int ql, int qr, long long val) {
        // 1) 전혀 겹치지 않으면 무시
        if (qr < l || r < ql) return;

        // 2) 완전히 포함되면: 현재 노드에만 갱신하고 lazy 기록
        if (ql <= l && r <= qr) {
            seg[idx]  += val * (r - l + 1); // 합 갱신: 구간 길이만큼 증가
            lazy[idx] += val;               // 밀린 업데이트 기록
            return;
        }

        // 3) 일부만 겹치면: 자식으로 내려가야 하므로 push
        push(idx, l, r);

        int mid = (l + r) >> 1;
        // 왼쪽/오른쪽으로 재귀 분할 갱신
        range_add(idx << 1,     l,       mid, ql, qr, val);
        range_add(idx << 1 | 1, mid + 1, r,   ql, qr, val);

        // 4) 자식 갱신 끝났으니 현재 노드 합 갱신
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1];
    }

    // 구간 [ql, qr]의 합 질의
    long long range_sum(int idx, int l, int r, int ql, int qr) {
        // 1) 불겹침
        if (qr < l || r < ql) return 0;

        // 2) 완전히 포함
        if (ql <= l && r <= qr) return seg[idx];

        // 3) 일부 겹침 → 내려가기 전 push
        push(idx, l, r);

        int mid = (l + r) >> 1;
        // 왼/오 합쳐서 반환
        return range_sum(idx << 1,     l,       mid, ql, qr)
             + range_sum(idx << 1 | 1, mid + 1, r,   ql, qr);
    }

    // ===== 외부에서 쓰기 쉬운 래퍼들 =====
    void build(const vector<long long>& a) { build(a, 1, 1, n); }
    void range_add(int l, int r, long long val) { range_add(1, 1, n, l, r, val); }
    long long point_query(int x) { return range_sum(1, 1, n, x, x); } // [x,x] 합 = A[x]
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    // 입력 배열: 1-indexed로 맞춤
    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    // 세그먼트 트리 구성
    SegTree st(N);
    st.build(A);

    int M; 
    cin >> M;
    while (M--) {
        int t; 
        cin >> t;
        if (t == 1) {
            // 1 i j k : A[i..j]에 k 더하기 (구간 업데이트)
            int i, j; long long k;
            cin >> i >> j >> k;
            st.range_add(i, j, k);
        } else {
            // 2 x : A[x] 출력 (점 질의 = [x,x] 합)
            int x; 
            cin >> x;
            cout << st.point_query(x) << '\n';
        }
    }
    return 0;
}
