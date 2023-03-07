#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> height(9, 0);
vector<int> ans;
bool done = false;

void bt(int cnt, int num, int sum) {
    if (done) return ;

    if (cnt == 7 && sum == 100) {
        // 답 출력
        sort(ans.begin(), ans.end());
        for (int i = 0; i < 7; ++i) {
            cout << ans[i] << '\n';
        }
        done = true;
        return ;
    }

    if (num >= 9 || sum > 100) {
        return ;
    }

    // 넣음
    ans.push_back(height[num]);
    bt(cnt+1, num+1, sum+height[num]);
    ans.pop_back();

    // 안 넣음
    bt(cnt, num+1, sum);
}

int main() {
    /* INPUT */
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    for (int i = 0; i < 9; ++i) {
        cin >> height[i];
    }

    /* SOLUTION */
    bt(0, 0, 0);

    return 0;
}