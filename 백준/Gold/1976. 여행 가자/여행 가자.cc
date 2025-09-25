#include <iostream>
#include <bits/stdc++.h>
using namespace std;
vector<int> parent, sz;  // 전역 parent 배열

// find 함수 (경로 압축 포함)
int findUF(int x) {
    if (parent[x] != x) parent[x] = findUF(parent[x]);
    return parent[x];
}

// union 함수
void unite(int a, int b) {
    int ra = findUF(a),  rb = findUF(b);
    if (ra == rb) return;
    // size 확인 후 , ra, rb 갱신
    if (sz[rb] > sz[ra]) swap(ra, rb);

    // parent 갱신 size 갱신
    parent[rb] = parent[ra];
    sz[ra] += sz[rb];
}



int main() {
    // freopen("input.txt", "r", stdin);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // n, m
    int n, m;
    cin >> n >> m;
    // 인접 행렬
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    // arrive
    vector<int> arrive(m);
    for (int i = 0; i < m; i++) {
        cin >> arrive[i];
        --arrive[i]; // 0 base 처리
    }

    // resize
    parent.resize(n);
    sz.resize(n);
    // 0부터 n까지 parent 초기값 갱신
    iota(parent.begin(), parent.end(), 0);

    // union 실행
    for (int i = 0; i < n; i++) {
        for (int j =0; j < n; j++) {
            if (arr[i][j] == 1) {
                unite(i, j);
            }
        }
    }

    // find하기
    string ans = "YES";
    int target = findUF(arrive[0]);
    for (int i = 1; i < m; i++) {
        if (target != findUF(arrive[i])) {
            ans = "NO";
            break;
        }
    }
    cout << ans << endl;;
}

