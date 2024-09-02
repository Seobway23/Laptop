#include <iostream>
using namespace std;

int main() {
    int n, r, c;
    cin >> n;
    
    for (int t = 0; t < n; t++) {
        cin >> r >> c;
        
        char arr[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> arr[i][j];
            }
        }
        
        int ans = 0;
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) { 
                if (j+2<c && arr[i][j] == '>' && arr[i][j+1] == 'o' && arr[i][j+2] == '<'){
                    ans++;
                }
                
                if (i +2 <r && arr[i][j] =='v' && arr[i+1][j] == 'o' && arr[i+2][j] == '^'){
                    ans++;
                }
            }
        }
        
        cout << ans << endl;
    }
    
    return 0;
}