#include <iostream>
#include <algorithm>

using namespace  std;
int main() {

    int n, k;
    int ans = -1000;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n-k + 1; i++) {
        int cnt = 0;
        for (int j = i; j < i + k; j++) {
            cnt += arr[j];
        }
        if (cnt > ans) {
            ans = cnt;
        }
    }

    cout << ans;
    return 0;
}