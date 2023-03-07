#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int N;
int house[26][26];
int visited[26][26];
vector<int> v;
void input() {
    cin >> N;
    string s;
    for (int i = 0; i < N; i++) {
        cin >> s;
        for (int j = 0; j < N; j++) {
            house[i][j] = s[j] - '0';
        }
    }
}
int dfs(int r, int c, int value) {
    //종료 조건
    if (r < 0 || r >= 25 || c < 0 || r >= 25) {
        return value;
    }
    if (house[r][c] != 1 || visited[r][c] == 1) {
        return value;
    }
    visited[r][c] = 1;
    value += 1;
    //상
    value = dfs(r - 1, c, value);
    //하
    value = dfs(r + 1, c, value);
    //좌
    value = dfs(r, c - 1, value);
    //우
    value = dfs(r, c + 1, value);
    return value;
}
void solution() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (house[i][j] == 1 && visited[i][j] == 0) {
                int tmp = dfs(i, j, 0);
                if(tmp != 0)
                    v.push_back(tmp);
            }
        }
    }
    sort(v.begin(), v.end());
    cout << v.size() << '\n';
    for (int k = 0; k < v.size(); k++) {
        cout << v[k] << '\n';
    }
}
int main() {
    input();
    solution();
}
