#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, ans = 0;
vector<pair<int, int> > list;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> N;
    int a, b;
    while (N--) {
        cin >> a >> b;
        list.push_back(make_pair(a, b));
    }

    /* SOLUTION */
    sort(list.begin(), list.end());
    
    int start_time = -1, end_time = -1;
    int cur_start, cur_end;
    for (int i = 0; i < list.size(); ++i) {
        cur_start = list[i].first;
        cur_end = list[i].second;

        if (end_time > cur_start) { // 진행중인 회의가 끝나는 시각이 현재 회의의 시작 시각보다 느리다면,
            if (end_time > cur_end) { // 진행중인 회의가 끝나는 시각이 현재 회의가 끝나는 시각보다 느리다면 
                start_time = cur_start; // 진행중인 회의를 그만두고, 현재 회의가 들어가도록 한다. -> 현재 회의가 들어가면서 끝나는 시각이 빨라지고, 다음 회의가 들어올수있는 경우가 늘어남 (greedy)
                end_time = cur_end;
            }
        }
        else { // 진행중인 회의가 끝나는 시각이 현재 회의의 시작 시각보다 빠르다면,
            start_time = cur_start; // 새 회의가 시작되므로 ans 를 1 증가.
            end_time = cur_end;
            ++ans;
        }

        // cout << i << "(" << cur_start << "," << cur_end << ") " << ans << '\n';
    }

    cout << ans;

    return 0;
}