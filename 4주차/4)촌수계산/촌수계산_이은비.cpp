#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int n, p1, p2, m, x, y;
vector<int> ver[101];
bool visitied[101];
queue<pair<int, int> > que;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> n >> p1 >> p2 >> m;
    while (m--) {
        cin >> x >> y;
        ver[x].push_back(y);
        ver[y].push_back(x);
    }

    /* SOLUTION */
    que.push(make_pair(0, p1));
    visitied[p1] = true;

    int step, node;
    while (!que.empty()) {
        step = que.front().first;
        node = que.front().second;
        que.pop();

        for (int i = 0; i < ver[node].size(); ++i) {
            int nxt_node = ver[node][i]; 
            if (!visitied[nxt_node]) {
                if (nxt_node == p2) {
                    cout << step+1;
                    return 0;
                }
                que.push(make_pair(step+1, nxt_node));
                visitied[nxt_node] = true;
            }
        }
    }

    cout << -1;

    return 0;
}