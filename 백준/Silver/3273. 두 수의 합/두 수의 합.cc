#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int target;
    cin >> target;

    // 투포인터 조건 i<j  and 정렬
    sort(arr, arr+ n);

    int left = 0, right = n-1, cnt = 0;

    while (left < right) {// 왜 =은 포하하지 않을까 -> 두개 비교해야 하는데 하나가 되기 때문!

        int sm = arr[left] + arr[right];

        if (sm == target) {
            cnt++, right--, left++;
        }

        else if (sm < target) {
            left++;
        }

        else {
            right--;
        }

    }


    cout << cnt << endl;

    return 0;
}