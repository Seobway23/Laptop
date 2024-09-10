#include <iostream>
#include <algorithm>

using namespace std;

bool canDistribute(const int jewels[], int m, int n, int maxJealousy) {
    int neededStudents = 0;
    for (int i = 0; i < m; i++) {
        neededStudents += (jewels[i] + maxJealousy - 1) / maxJealousy;
        if (neededStudents > n) {
            return false;
        }
    }
    return true;
}

int main() {
    int n, m;
    cin >> n >> m;
    int jewels[m];

    int maxJewels = 0;
    for (int i = 0; i < m; i++) {
        cin >> jewels[i];
        maxJewels = max(maxJewels, jewels[i]);
    }

    int low = 1, high = maxJewels, result = maxJewels;

    while (low <= high) {
        int mid = (low + high) / 2;
        if (canDistribute(jewels, m, n, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << result << endl;

    return 0;
}
