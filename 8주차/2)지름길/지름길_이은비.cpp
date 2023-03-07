#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define INF 987654321

int N, D, a, b, c;

vector<pair<int, int> > edge[10001]; // [node1] = (node2, cost)
int dist[10001];


void dijk() {
    for (int i = 0; i <= D; i++) {
        dist[i] = INF;
        edge[i].push_back(make_pair(i+1, 1));
    }

    priority_queue<pair<int, int> > que;

    dist[0] = 0;
    que.push(make_pair(0, 0));
    
    while (!que.empty()) {
        int tnode = que.top().second; int tcost = que.top().first;
        que.pop();

        for (int i = 0; i < edge[tnode].size(); i++) {
            
            int nnode = edge[tnode][i].first; int ncost = edge[tnode][i].second + tcost;
            if (ncost < dist[nnode]) {
                dist[nnode] = ncost;
                que.push(make_pair(ncost, nnode));
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> D;
    for (int i = 0; i < N; ++i) {
        cin >> a >> b >> c; // 시작 위치, 도착 위치, 지름길 길이
        edge[a].push_back(make_pair(b, c));
    }


    dijk();
    cout << dist[D];
    return 0;
}