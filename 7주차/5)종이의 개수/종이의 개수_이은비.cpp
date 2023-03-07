#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int board[2187][2187];
int answer[3] = {0, 0, 0};

void divide_paper(int x, int y, int n) {
    int check = board[x][y];
    for (int i = x; i < x+n; ++i) {
        for (int j = y; j < y+n; ++j) {
            if (check != board[i][j]) {
                for (int k = 0; k < 9; ++k) { // 나머지 | 몫
                    divide_paper(x+((k%3)*(n/3)), y+((k/3)*(n/3)), n/3);
                }
                return ;
            }
        }
    }

    ++answer[check+1];
}


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> board[i][j];
        }
    }

    divide_paper(0, 0, N);
    for (int i = 0; i < 3; ++i) {
        cout << answer[i] << '\n';
    }

    return 0;
}