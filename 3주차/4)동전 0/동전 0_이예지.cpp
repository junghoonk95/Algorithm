#include <iostream>
#include <vector>
using namespace std;

//코인 가치 저장 
vector<int> coin_val;

int main() {
	int n,k,x;
	cin >> n >> k;

	for(int i =0; i<n; i++) {
		cin >> x;
        coin_val.push_back(x);
	}
    
    //코인 개수
	int count = 0;
    
    //뒤에서 부터 돌기
	for(int i = n-1; i >= 0; i--) {
		count += k/coin_val[i]; // 몫 = 쓰는 코인 개수
		k = k % coin_val[i]; // 남은 가치
		if(k==0) break;	
	}
	cout << count << endl;
    return 0;
}
