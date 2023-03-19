#include <iostream>
#include <vector>
#include <algorithm>
#define INF 987654321
using namespace std;

int n, s, dp[301][3];
int score[301];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> score[i];
    }

    dp[1][1] = score[1];
    
    for (int i = 2; i <= n; ++i) {
        // dp[i][0] = max(dp[i-1][2], max(dp[i-1][1], dp[i-1][0]));
        dp[i][1] = max(dp[i-2][2], dp[i-2][1]) + score[i];
        dp[i][2] = dp[i-1][1] + score[i];
    }

    cout << max(dp[n][1], dp[n][2]);

    return 0;
}