#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int arr[10];
int sum = 0;

int main() {
	//입력받기
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	sort(arr, arr + 9);
	// 9에서 2명 뽑기 => 9C2 = 36
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			//난쟁이 아닌애들 찾으면
			if (sum - (arr[i] + arr[j]) == 100) {
				//출력
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j)
						continue;
					cout << arr[k] << endl;
				}
				//끝
				return 0;
			}
		}
	}
}
