#include <iostream>
using namespace std;

int main()
{
    int coins, mx;
    
    cin >> coins >> mx;
    
    if (coins * 100 >= mx) {
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    } 
    
    return 0;
}