#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, cnt = 0, ans = 0;
vector<int> times;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;

    int a;
    for (int i = 0; i < N; ++i) {
        cin >> a;
        times.push_back(a);
    }

    sort(times.begin(), times.end());

    for (int i = 0; i < N; ++i) {
        cnt += times[i];
        ans += cnt;
    }

    cout << ans;

    return 0;
}