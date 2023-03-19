#include <iostream>
#include <vector>
using namespace std;
int k,n; //아파트 층, 호수
int arr[15][15] = {0,};
vector<int> answer;

int main(){
    int T;
    cin >> T;
    
    //0층
    for(int i=1; i<=15; i++){
        arr[0][i] = i;
    }
    
    //1층부터 15층의 1호~15호 
    for(int i=1; i<=15; i++){
        // 각 층 0호 0으로 초기화 
        arr[i][0] = 0;
        for(int j=1; j<=15; j++){
            arr[i][j] = arr[i][j-1] + arr[i-1][j];
        }
    }
    
    for(int i=0; i<T; i++){
        cin >> k >> n;
        answer.push_back(arr[k][n]);
    }
    for(int i=0; i<T; i++){
        cout << answer[i] << endl;
    }
    
    return 0;
}
