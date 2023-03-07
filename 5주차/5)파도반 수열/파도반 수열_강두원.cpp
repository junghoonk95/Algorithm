#include<iostream>

using namespace std;

long long dp[101] = {0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, };

int T, N;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    for(int i = 10; i < 101; ++i) {
        dp[i] = dp[i-2] + dp[i-3];
    }

    cin >> T;

    for(int t = 0; t < T; ++t) {
        cin >> N;
        cout << dp[N] << "\n";
    }
}
