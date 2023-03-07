#include <iostream>
#include <vector>
#include <algorithm>
#define INF 987654321
using namespace std;

int N;
int dp[1000002];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;

    fill(dp, dp+1000001, INF);
    dp[1] = 0;
    
    for (int i = 1; i < N; ++i) {
        if (i*3 < 1000001) dp[i*3] = min(dp[i*3], dp[i]+1);
        if (i*2 < 1000001) dp[i*2] = min(dp[i*2], dp[i]+1); // if
        dp[i+1] = min(dp[i+1], dp[i]+1);
    }

    cout << dp[N];

    return 0;
}