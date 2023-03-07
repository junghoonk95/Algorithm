#include<iostream>
#include<vector>
#include<climits>

using namespace std;
typedef long long ll;

int N, T;

vector<vector<int>> dp;
vector<int> table;


int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    // freopen("input.txt", "r", stdin);

    // cin >> T;
    T = 1;

    for(int t = 1; t <= T; ++t) {
        cin >> N;
        vector<vector<int>>(N+1, vector<int>(2, 0)).swap(dp);
        vector<int>(N+1, 0).swap(table);

        for(int i = 1; i <= N; ++i) {
            cin >> table[i];
        }

        dp[1][0] = table[1];
        for(int i = 2; i <= N; ++i) {
            dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + table[i];
            dp[i][1] = dp[i-1][0] + table[i];
        }
        
        cout << max(dp[N][0], dp[N][1]) << "\n";
    }
}
