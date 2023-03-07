#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K;
vector<pair<int, int> > item(100002);
int dp[100002][102]; // dp[i][j] : 가방의 현재 무게가 i 이고, j번째 아이템까지 넣을지말지 여부를 판단했을 때의 가방의 가치.

int ans = 0;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> N >> K;
    
    for (int i = 1; i <= N; ++i) {
        cin >> item[i].first >> item[i].second;
    }

    /* SOLUTION */
    for (int i = 1; i <= N; ++i) {
        int w = item[i].first;
        int v = item[i].second;

        for (int j = 1; j <= K; ++j) {
            if (j-w >= 0) { // 가방에 담을 수 있다면
                /*
                 * (1) dp[j-w][i-1]+v : 가방 무게가 j 인데, 가방에 i번째 아이템을 담았을 때
                 *  i번째 아이템을 담았을 때의 무게가 j 이므로, 무게가 j-w 이고, i-1번째 아이템까지 여부를 결정했을 때의 최적해에 + i번째 아이템 가치를 더한다.
                 * (2) dp[j][i-1] : 가방 무게가 j 인데, 가방에 i번째 아이템을 담지 않았을 때
                 *  무게가 j이고, i-1번째 아이템까지 여부를 결정했을 때의 최적해
                */
                dp[j][i] = max(dp[j-w][i-1]+v, dp[j][i-1]);
            }
            else { // 가방에 담을 수 없는 무게.
                dp[j][i] = dp[j][i-1];
            }
        }
    }

    cout << dp[K][N];

    return 0;
}