#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 투포인터 초기화
    int start = 0, end = 0;
    int current_sum = 0, count = 0;
    
    while (end <= n) {
        if (current_sum < m) {
            if (end == n) break;
            current_sum += arr[end];
            end++;
        } else if (current_sum > m) {
            current_sum -= arr[start];
            start++;
        } else { // current_sum == m
            count++;
            current_sum -= arr[start];
            start++;
        }
    }

    cout << count << endl;
    return 0;
}
