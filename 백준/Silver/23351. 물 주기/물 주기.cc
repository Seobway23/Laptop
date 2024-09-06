#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int n, k, a, b;
    cin >> n >> k >> a >> b;

    int arr[n];
    fill_n(arr, n, k);

    int time =0;
    bool flag = false;
    while (true) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                flag =  true;
                break;
            }
        }
        if (flag) {
            break;
        }
        sort(arr, arr + n);

        // 물주기
        for (int i = 0; i < a; i++) {
            arr[i] += b;
        }

        // -1
        for (int i = 0; i < n; i++) {
            arr[i] -=1;
        }
        time +=1;
    }


    cout << time;
    return 0;

}