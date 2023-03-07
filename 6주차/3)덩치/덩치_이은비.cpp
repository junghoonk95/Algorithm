#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, x, y;
vector<pair<int, int> > people;
vector<int> ans;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        people.push_back(make_pair(x, y));
    }

    int k = 0;
    for (int i = 0; i < n; ++i) {
        k = 0;
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                if (people[i].first < people[j].first && people[i].second < people[j].second) {
                    ++k;
                }
            }
        }
        cout << k+1 << '\n';
    }

    return 0;
}