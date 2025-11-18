#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("input.txt", "r", stdin);


    int n, k;
    cin >> n >> k;

    vector<int> dp(k + 1, 0);

    for (int i = 0; i < n; i ++) {
        int W, V;
        cin >> W >> V;

        for (int w = k; w>=W; w--) {
            dp[w] = max(dp[w], dp[w-W] + V);
        }
    }

    cout << dp[k] << endl;

    return 0;
}
