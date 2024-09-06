#include <iostream>
#include <vector>

using namespace std;

// unique 인지 판별하는 함수
bool isUnique(int num) {
    bool arr[10] = {false};

    while (num >0) {
        int target =  num % 10;
        if (arr[target]) {
            return false;
        }
        arr[target] = true;
        num /= 10;
    }
    return true;
}

int main() {

    // 연속X 리스트 만들기
    vector<int> uniqueList;
    uniqueList.reserve(1000000);

    for(int i = 1; uniqueList.size() < 1000000; i++) {
        if (isUnique(i)) {
            uniqueList.push_back(i);
        }
    }
    int n;
    while (true) {
        cin >> n;

        if (n==0) {
            return 0;
        }
        cout << uniqueList[n-1]<< endl;
    }
}