#include <iostream>
#include <vector>

using namespace std;

bool findUnique(int num) {
    bool digits[10] = {false}; // 각 자릿수를 추적하는 배열

    while (num > 0) {
        int digit = num % 10;
        if (digits[digit]) {
            return false; // 중복된 자릿수 발견
        }
        digits[digit] = true;
        num /= 10;
    }
    return true;
}

int main() {
    vector<int> nums;
    nums.reserve(1000000);

    for (int i = 1; nums.size() < 1000000; i++) {
        if (findUnique(i)) {
            nums.push_back(i);
        }
    }

    int n;
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
        cout << nums[n - 1] << endl; // 미리 계산된 값에서 인덱스 접근
    }

    return 0;
}
