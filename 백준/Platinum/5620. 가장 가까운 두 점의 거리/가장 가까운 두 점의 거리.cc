#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Point {
    long long x, y; // 64 bit 정수 좌표
};

long long dist2(const Point &a, const Point &b) {
    const long long dx = a.x - b.x;
    const long long dy = a.y - b.y;
    return dx * dx + dy * dy;
}

// 3개 이하일 경우, 3개는 직접 계산하기
long long bruteForce(vector<Point> &p, int l, int r) {
    long long best = LLONG_MAX;

    // best 구하기
    for (int i = l; i <= r; i++) {
        for (int j = i + 1; j <= r; j++) {
            best = min(best, dist2(p[i], p[j]));
        }
    }

    // y좌표 sort 후 넘겨주기
    sort(p.begin() + l, p.begin() + r + 1, [](const Point &a, const Point &b){return a.y < b.y;});
    return best;
}

// 분할 정복
long long closest(vector<Point> &p, int l, int r) {
    // 현재 분할 vector의 갯수
    int n = r - l + 1;
    if (n <= 3) return bruteForce(p, l, r);

    int mid = ( l + r) / 2;
    long long midX = p[mid].x;

    // left, right 하위 문제
    long long dL = closest(p,l, mid);
    long long dR = closest(p, mid + 1, r);
    long long d2 = min(dL, dR);

    // 하위 구간 y 기준 선형 병합
    vector<Point> merged;
    merged.reserve(n);
    merge(p.begin() + l, p.begin() + mid + 1,
        p.begin() + mid + 1, p.begin() + r + 1,
        back_inserter(merged),
        [](const Point &a, const Point &b) {return a.y < b.y;});


    // 부모도 y 정렬 쓸 수 있도록 원래 구간에 덮어쓰기
    copy(merged.begin(), merged.end(), p.begin() + l);

    // strip => mid 근처 +-델타 이내 범위 확인
    vector<Point> strip;
    strip.reserve(n);
    for (const auto &pt : merged) {
        long long dx = pt.x - midX;
        if (dx * dx < d2) strip.push_back(pt);
    }

    // 비교
    for (int i = 0; i < static_cast<int>(strip.size()); ++i) {
        for(int j = i + 1; j < static_cast<int>(strip.size()) && j<= i + 7; ++j) {
            const long long dy = strip[j].y - strip[i].y;
            if (dy * dy >= d2) break;
            d2 = min(d2, dist2(strip[i], strip[j]));
        }
    }
    return d2;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {return 0;}
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;

    // 최초 1회 x 정렬
    sort(p.begin(), p.end(),
        [](const Point &a, const Point &b) {
            if (a.x != b.x) return a.x < b.x;
            return a.y < b.y;
        });

    // 제곱 거리 출력
    cout << closest(p, 0, n - 1) << endl;
    return 0;
}