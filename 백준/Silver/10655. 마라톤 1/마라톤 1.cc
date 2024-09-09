#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

// 맨해튼 거리 계산 함수
int manhattanDistance(pair<int, int> a, pair<int, int> b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    // 전체 경로의 총 거리 계산
    int totalDistance = 0;
    for (int i = 1; i < n; i++) {
        totalDistance += manhattanDistance(points[i - 1], points[i]);
    }

    // 각 체크포인트를 건너뛰었을 때의 거리 계산
    int minDistance = totalDistance;
    for (int i = 1; i < n - 1; i++) { // 1번과 N번 체크포인트는 건너뛸 수 없으므로 i = 1부터 n-2까지
        int distanceWithSkip = totalDistance
                               - manhattanDistance(points[i - 1], points[i])
                               - manhattanDistance(points[i], points[i + 1])
                               + manhattanDistance(points[i - 1], points[i + 1]);

        minDistance = min(minDistance, distanceWithSkip);
    }

    cout << minDistance << endl;
    return 0;
}
