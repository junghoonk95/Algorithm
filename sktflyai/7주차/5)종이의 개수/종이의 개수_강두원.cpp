#include<iostream>
#include<algorithm>
#define MAX 2200

using namespace std;

int tb[MAX][MAX];

int answer[] = {0, 0, 0};
int dx[] = {0, 1, 2, 0, 1, 2, 0, 1, 2};
int dy[] = {0, 0, 0, 1, 1, 1, 2, 2, 2};

void dc(int x, int y, int level) {
    if(level == 0) return;

    int target = tb[y][x];
    int flag = 0;
    for(int i = y; i < y + level; ++i) {
        for(int j = x; j < x + level; ++j) {
            if(target != tb[i][j]) {
                flag = 1;
                break;
            }
        }
        if(flag == 1) break;
    }

    if(!flag) answer[target+1]++;
    else 
        for(int i = 0; i < 9; ++i)
            dc(x + dx[i]*(level/3), y + dy[i]*(level/3), level/3);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;

    cin >> N;

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> tb[i][j];
        }
    }

    dc(0, 0, N);
    
    for(int i = 0; i < 3; ++i) cout << answer[i] << "\n";
}
