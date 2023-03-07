#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

pair<int,int> arr[50];

int main() {
	int N;
	cin >> N;

	//입력받기
	for(int i = 0; i < N; i++) {
		cin >> arr[i].first >> arr[i].second;
	}

	//덩치 1등에서 시작
	int rank = 1;

	//각 pair마다 모든 경우 다 비교(리그)
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			//덩치가 작으면 랭크 내려감
			if (arr[i].first < arr[j].first && arr[i].second < arr[j].second)
				rank++;
		}
		cout << rank << " ";
		rank = 1;
	}


    return 0;
}
