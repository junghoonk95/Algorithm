#include<iostream>

using namespace std;
#define MAX (1 << 7) + 1
int N;
int tb[MAX][MAX];

int blue, white;

void dc(int x, int y, int level) {
    int cnt = 0;

    for(int i = x; i < x + level; ++i) {
        for(int j = y; j < y + level; ++j) {
            if(tb[i][j]) cnt++;
        }
    }

    if(cnt==0) white++;
    else if(cnt == level*level) blue++;
    else {
        dc(x, y, level/2);
        dc(x, y + level/2, level/2);
        dc(x + level/2, y, level/2);
        dc(x + level/2, y + level/2, level/2);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> tb[i][j];
        }
    }
    dc(0, 0, N);
    cout << white << "\n" << blue << "\n";
}

/*
0 0
0 0

1 0  0 1  0 0  0 0
0 0  0 0  1 0  0 1

1 1  1 0  1 0  0 1  0 1  0 0
0 0  1 0  0 1  1 0  0 1  1 1

1 1  1 1  1 0  0 1
1 0  0 1  1 1  1 1

1 1
1 1
*/
