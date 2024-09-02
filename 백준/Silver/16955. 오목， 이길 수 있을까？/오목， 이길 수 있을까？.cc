#include <iostream>
#include <cstring>
using namespace std;

int main() {
    // init 
    char arr[10][10];
    int cntdot;
    int cntx;
    bool ans = false;
    // 입력 받기
    
    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            cin >> arr[i][j];
        }
    }
    
    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            // 오른쪽
            cntdot = 0;
            cntx = 0;
            for(int k=0; k<5;k++){
                int nj = j + k;
                
                if (nj < 10) {
                    if (arr[i][nj] == 'X'){
                        cntx ++;
                    }
                    else if(arr[i][nj] == '.'){
                        cntdot ++;
                    }
                }
            }
            if (cntdot ==1 and cntx ==4){
                ans = true;
            }
            
            // 아래
            cntdot = 0;
            cntx = 0;
            for(int k=0; k<5; k++){
                int ni = i + k;
                
                if (ni <10) {
                    if(arr[ni][j] == 'X'){
                        cntx ++;
                    }
                    
                    else if (arr[ni][j] == '.'){
                        cntdot ++;
                    }
                }
            }
            
            if (cntdot ==1 and cntx ==4){
                ans = true;
            }
            
            // 대각선 아래
            cntdot = 0;
            cntx = 0;
            for(int k=0; k<5; k++){
                int ni = i + k;
                int nj = j + k;
                
                if (ni < 10 and nj <10){
                    if(arr[ni][nj] == 'X'){
                        cntx ++;
                    }
                    
                    else if (arr[ni][nj] == '.'){
                        cntdot ++;
                    }
                }
            }
            
            if (cntdot ==1 and cntx ==4){
                ans = true;
            }
            
            
            // 대각선 위
            cntdot = 0;
            cntx = 0;
            for(int k=0; k<5; k++){
                int ni = i - k;
                int nj = j + k;
                
                if ( 0 <= ni < 10 and nj <10){
                    if(arr[ni][nj] == 'X'){
                        cntx ++;
                    }
                    
                    else if (arr[ni][nj] == '.'){
                        cntdot ++;
                    }
                }
            }
            
            if (cntdot ==1 and cntx ==4){
                ans = true;
            }
            
            
            
        }   
        
        
        if (ans == true){
            cout << 1 << endl;
            return 0;
        }
    }
    
    
    
    
    
    cout << 0 << endl;
    return 0;
}
