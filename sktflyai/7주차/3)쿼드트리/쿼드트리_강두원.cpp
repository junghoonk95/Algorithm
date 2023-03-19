#include<iostream>

using namespace std;
#define MAX 64
int N;
int tb[MAX][MAX];

void dc(int x, int y, int level) {
    int std = tb[y][x];
    bool flag = true;

    for(int i = 0; i < level; ++i) {
        for(int j = 0; j < level; ++j) {
            if(std != tb[y + i][x + j]) {
                flag = false;
                break;
            }
        }
        if(flag == false) break;
    }

    if(flag) cout << std;
    else {
        cout << "(";
        dc(x, y, level/2);
        dc(x + level/2, y, level/2);
        dc(x, y + level/2, level/2);
        dc(x + level/2, y + level/2, level/2);
        cout << ")";
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    string temp;
    for(int i = 0; i < N; ++i) {
        cin >> temp;
        for(int j = 0; j < temp.size(); ++j) {
            tb[i][j] = temp[j] - '0';
        }
    }

    dc(0, 0, N);
    cout << "\n";
}
