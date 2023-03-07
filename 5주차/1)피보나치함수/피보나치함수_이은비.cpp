#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, N;
    // 0 : 1 0
    // 1 : 0 1
    // 2 : 1 1
    // 3 : 1 2
    // 4 : 2 3
    // 5 : 3 5
    // 6 : 5 8
int dp[41][2];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    dp[0][0] = 1; dp[0][1] = 0;
    dp[1][0] = 0; dp[1][1] = 1;
    for (int i = 2; i < 41; ++i) {
        dp[i][0] = dp[i-1][0] + dp[i-2][0];
        dp[i][1] = dp[i-1][1] + dp[i-2][1];
    }

    cin >> T;
    while (T--) {
        cin >> N;
        cout << dp[N][0] << ' ' << dp[N][1] << '\n';
    }

    return 0;
}