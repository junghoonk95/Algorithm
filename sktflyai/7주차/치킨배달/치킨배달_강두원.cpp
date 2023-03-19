#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>

using namespace std;
const int N = 51;
int n, m, answer = INT_MAX;
int tb[N][N];
vector<pair<int, int>> chicken;
vector<pair<int, int>> house;
vector<int> vst;

int calc_dist(vector<pair<int, int>> path) {
    vector<int> temp(house.size(), INT_MAX);
    for (int i = 0; i < house.size(); i++) {
        for (int j = 0; j < path.size(); j++) {
            temp[i] = min(temp[i], abs(house[i].first - path[j].first) + abs(house[i].second - path[j].second));
        }
    }
    int sum = 0;
    for(int i = 0; i < temp.size(); ++i) {
        sum += temp[i];
    }
    return sum;
}

void pick(int cur, vector<pair<int, int>> path) {
    if(path.size() == m) {
        answer = min(answer, calc_dist(path));
        return;
    }

    for(int i = cur; i < chicken.size(); ++i) {
        if(vst[i] == 1) continue;
        vector<pair<int, int>> nPath(path);
        nPath.emplace_back(chicken[i]);
        vst[i] = 1;
        pick(i, nPath);
        vst[i] = 0;
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> tb[i][j];
            if (tb[i][j] == 1) house.emplace_back(j, i);
            if (tb[i][j] == 2) chicken.emplace_back(j, i);
        }
    }
    vector<int>(chicken.size()).swap(vst);
    pick(0, vector<pair<int, int>>());
    cout << answer << endl;
    return 0;
}
