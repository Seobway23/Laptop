#include <iostream>
#include <string>

using namespace std;
int main() {
    int n;
    cin >> n;

    for (int i=0; i<n; i++){
        string st;
        cin >> st;

        cout << st[0] << st[st.size()-1] << endl;
    }
}
