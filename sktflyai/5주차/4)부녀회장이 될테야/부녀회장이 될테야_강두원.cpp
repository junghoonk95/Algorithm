#include<iostream>

using namespace std;

int T;
int N, K;
int dp[15][15];

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    for(int i = 0; i < 15; ++i) {
            dp[i][1] = 1;
            dp[0][i] = i;
    }

    for(int i = 1; i < 15; ++i) {
        for(int j = 2; j < 15; ++j) {
            dp[i][j] = dp[i][j-1] + dp[i-1][j];
        }
    }

    cin >> T;

    for(int t = 0; t < T; ++t) {
        cin >> N >> K;

        cout << dp[N][K] << "\n";
    }
}
