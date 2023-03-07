#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N, D;
vector<vector<int>> highway;
int map[10000] = {
    0,
};
bool cmp(vector<int> a, vector<int> b) {
  return a[0] < b[0];
}
//입력부
void input() {
  cin >> N >> D;
  for (int i = 0; i < N; i++) {
    vector<int> v;
    int sp, ep, len;
    cin >> sp >> ep >> len;
    v.push_back(sp);
    v.push_back(ep);
    v.push_back(len);
    highway.push_back(v);
  }
}
void solution() {
  int result = 20000;
  int shortcut_idx = 0;
  sort(highway.begin(), highway.end(), cmp);
  for (int i = 0; i <= D; i++) {
    //현재 위치 갱신
    if (i != 0) {
      if (map[i] == 0) {
        map[i] = map[i - 1] + 1;
      } else {
        map[i] = min(map[i - 1] + 1, map[i]);
      }
    }

    //지름길인 경우 추가 갱신
    if (shortcut_idx < highway.size()) {
      for (; highway[shortcut_idx][0] == i;) {
        int new_dist = map[i] + highway[shortcut_idx][2];
        // cout << new_dist << endl;
        if (map[highway[shortcut_idx][1]] == 0) {
          map[highway[shortcut_idx][1]] = new_dist;
        } else {
          map[highway[shortcut_idx][1]] =
              min(map[highway[shortcut_idx][1]], new_dist);
        }
        shortcut_idx += 1;
        if (shortcut_idx == highway.size())
          break;
      }
    }
  }
  cout << map[D];
}

int main() {
  input();
  solution();
}
