#include <iostream>

using namespace std;

int N;
int main() {
	cin >> N; // Nkg 입력받기
	int answer = 0; // 봉지 개수
    //N이 양수일 동안 반복
	while (N>=0) {
		if (N%5 == 0) {	//5로 계속 나눔 -> 나누어 지면
			answer += (N/5); //몫을 더한 것이 정답
			cout << answer << endl;
			return 0;
		}
        // 5로 나누어지지 않는다면 
		N -= 3;	// 3kg을 빼기 
		answer++; // 봉지 추가
	}
	cout << -1 << endl;
}
