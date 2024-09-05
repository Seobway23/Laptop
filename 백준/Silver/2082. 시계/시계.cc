#include <iostream>
#include <vector>

using namespace std;
int main() {
    vector<string> pattern;
    string line;
    vector<vector<vector<int>>> visited = {
        {{1}, {1, 4}, {}},
        {{1, 2, 3, 7}, {}, {5, 6}},
        {{1,7}, {0, 1, 7}, {}},
        {{1, 3, 4, 5, 7, 9}, {}, {2}},
        {{1, 4, 7, 9}, {1, 4, 7, 9}, {}},
    };

    for (int i=0; i<5; i++) {
        getline(cin, line);
        pattern.push_back(line);
    }

    vector<int> ans(4,0);

    // 주어진 입력을 4칸 간격으로 처리
    for (int i=0; i<15; i+=4) {
        vector<int> arr(10, 0);
        for (int j=0; j<5; j++){
            for (int k=0; k<3; k++){  // 'j' 대신 'k'로 변경
                if (pattern[j][i + k] == '#') {
                    for (const auto& x : visited[j][k]){
                        arr[x]= 1;
                    }
                }
            }
        }

        for (int k=0; k<10; k++) {
            if (arr[k]== 0) {
                ans[i / 4] = k;
                break;
            }
        }
    }

    cout << ans[0] << ans[1] << ":" << ans[2] << ans[3];

    return 0;
}
