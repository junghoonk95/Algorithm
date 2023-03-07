#include<iostream>
#include<vector>

using namespace std;

int T, N;
vector<int> dp0, dp1;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    cin >> T;

    for(int t = 1; t <= T; ++t) {
        cin >> N;

        vector<int>(N+1 ,0).swap(dp0);
        vector<int>(N+1 ,0).swap(dp1);

        dp0[0] = 1;
        dp1[1] = 1;

        for(int i = 2; i <= N; ++i) {
            dp0[i] = dp0[i-1] + dp0[i-2];
            dp1[i] = dp1[i-1] + dp1[i-2];
        }

        cout << dp0[N] << " " << dp1[N] << "\n";
    }
}
