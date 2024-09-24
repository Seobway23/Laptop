#include <iostream>

using namespace std;
int main() {
    // 시간 제한 0.5초 => 최적화 시켜라!
    // 1. input
    int n, m;
    cin >> n >> m;

    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int s = 0, e = 0;
    int cur_sum = 0, cnt = 0;

    while (e <= n) {
        if (cur_sum < m) {
            if (e == n) break;
            cur_sum += arr[e];
            e++;
        }
        else if (cur_sum > m ) {
            cur_sum -= arr[s];
            s++;
        }
        else { // 같을 때
            cnt++;
            cur_sum -= arr[s];
            s++;
        }
    }

    cout << cnt << endl;

    return 0;
}