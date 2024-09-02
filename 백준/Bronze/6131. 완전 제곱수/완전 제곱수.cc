#include <iostream>
#include <cmath>

using namespace std;
int main() {
    int n;
    int ans = 0;
    cin >> n;
    
    for (int i=1; i < 501; i++) {
        for (int j=1; j < 501; j++) {
            
            if (pow(i, 2) == pow(j, 2) + n) {
                ans += 1;
            }
        }
    }
    
    cout << ans << endl;
    
    
    return 0;
}