#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K;
int ans = 0;
vector<int> money;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    int a;
    for (int i = 0; i < N; ++i) {
        cin >> a;
        money.push_back(a);
    }

    sort(money.begin(), money.end(), greater<int>());
    
    for (int i = 0; i < money.size(); ++i) {
        if (K == 0) break;
        if (K < money[i]) continue;

        ans += (K/money[i]);
        K = (K%money[i]);
    }

    cout << ans;

    return 0;
}