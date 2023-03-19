#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, k, n;
int room[15][15]; // room[i][j] : i층 j호에 사는 사람수
int dp[15][15]; // dp[i][j] : i층 j호까지 사는 사람의 전체 합

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> T;

    for (int i = 1; i < 15; ++i) {
            room[0][i] = i;
            dp[0][i] = dp[0][i-1] + room[0][i];
    }

    for (int i = 1; i < 15; ++i) {
        for (int j = 1; j < 15; ++j) {
            room[i][j] = dp[i-1][j];
            dp[i][j] = dp[i][j-1] + room[i][j];   
        }
    }

    while (T--) {
        cin >> k >> n;
        
        cout << room[k][n] << '\n';
    }

    return 0;
}

// 0 : 1 2 3 -> 1 3 6
// 1 : 1 3 6 -> 1 4 10
// 2 : 1 4 10
