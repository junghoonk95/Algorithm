#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, N, a, b, ans;
vector<pair<int, int> > list;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> T;
    
    while (T--) {
        ans = 1;
        cin >> N;

        for (int i = 0; i < N; ++i) {
            cin >> a >> b;
            list.push_back(make_pair(a, b));
        }

        sort(list.begin(), list.end());

        b = list[0].second;
        for (int i = 1; i < N; ++i) {
            if (list[i].second <= b) {
                ++ans;
                b = list[i].second;
            }
        }

        cout << ans << '\n';

        list.clear();
    }

    return 0;
}