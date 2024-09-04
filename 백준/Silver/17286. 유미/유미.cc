#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<vector<int>> arr(4, vector<int>(2));

double dist(int cur_i, int i){
    return sqrt(pow(arr[i][0] - arr[cur_i][0], 2) + pow(arr[i][1] - arr[cur_i][1], 2));
}

void findMin(int cnt, vector<int> &visit, int cur_i, double sm, vector<double> &results) {
    if (cnt == 3){
        results.push_back(sm);
        return;
    }
    
    for (int i = 1; i < 4; i++) {
        if (visit[i] == 0){
            visit[i] = 1;
            findMin(cnt + 1, visit, i, sm + dist(cur_i, i), results);
            visit[i] = 0;
        }
    }
}

int main() {
    for(int i = 0; i < 4; i++) {
        cin >> arr[i][0] >> arr[i][1];
    }
    
    vector<int> visit(4, 0);
    visit[0] = 1;
    vector<double> results;
    findMin(0, visit, 0, 0, results);
    
    sort(results.begin(), results.end());
    cout << static_cast<int>(results[0]) << endl; // 정수로 변환하여 출력
   

    return 0;
}
