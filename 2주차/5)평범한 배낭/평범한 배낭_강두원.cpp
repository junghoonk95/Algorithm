/*
Concept: dp

2차원 dp를 활용하여 각 물건이 추가될 때마다 가장 최적의 케이스 계산
점화식 : dp[i][j] = MAX(dp[i-1][j], v[i] + dp[i-1][j-w[i]]);
*/

#include<iostream>
#define MAX(a,b) a > b ? a: b

using namespace std;

int N, K;
int dp[101][100001];
int w[101];
int v[101];

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;

    for(int i = 1; i <= N; ++i) cin >> w[i] >> v[i];

    for(int i = 1; i <= N; ++i) {
        for(int j = 1; j <= K; ++j) {
            if (j >= w[i]) dp[i][j] = MAX(dp[i-1][j], v[i] + dp[i-1][j-w[i]]);
            else dp[i][j] = dp[i-1][j];
        }
    }
    cout << dp[N][K] << '\n';
}
