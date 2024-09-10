#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool can_distribute(const vector<long long>& jewels, long long N, long long mid) {
    long long count = 0;
    for (auto jewel : jewels) {
        count += (jewel + mid - 1) / mid;  // mid 이하의 개수로 나눌 때 필요한 학생 수
        if (count > N) return false;  // 학생 수를 초과하면 더 이상 계산할 필요 없음
    }
    return count <= N;
}

long long find_minimum_jealousy(long long N, const vector<long long>& jewels) {
    long long low = 1;
    long long high = *max_element(jewels.begin(), jewels.end());
    long long result = high;

    while (low <= high) {
        long long mid = (low + high) / 2;
        if (can_distribute(jewels, N, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return result;
}

int main() {
    long long N, M;
    cin >> N >> M;
    vector<long long> jewels(M);

    for (int i = 0; i < M; i++) {
        cin >> jewels[i];
    }

    cout << find_minimum_jealousy(N, jewels) << endl;
    return 0;
}