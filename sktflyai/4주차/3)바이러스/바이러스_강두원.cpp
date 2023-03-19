#include<iostream>
#include<queue>
#include<vector>

using namespace std;

queue<int> q;
int N, V;
vector<vector<int>> graph;
int vst[101];
int answer;

void bfs(int s){
    queue<int>().swap(q);
    answer = -1;

    q.emplace(s);
    vst[s] = 1;

    while(q.size()) {
        int cur = q.front();
        q.pop();

        answer++;

        for(auto nxt: graph[cur]) {
            if(vst[nxt] == 0) {
                vst[nxt] = 1;
                q.emplace(nxt);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> V;
    vector<vector<int>>(N+1, vector<int>()).swap(graph);

    int t1, t2;
    for(int i = 0; i < V; ++i) {
        cin >> t1 >> t2;
        graph[t1].emplace_back(t2);
        graph[t2].emplace_back(t1);
    }
    bfs(1);
    cout << answer << "\n";
}
