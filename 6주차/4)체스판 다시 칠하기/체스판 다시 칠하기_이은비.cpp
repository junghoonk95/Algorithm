#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define INF 987654321

int M, N, ans = INF;
char board[50][50];
char color[2] = {'W', 'B'};

int fill_board(int x, int y) {
    int rnt_cnt = INF, cnt = 0;

    for (int c = 0; c < 2; ++c) {
        cnt = 0;
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j) {
                if (board[i+x][j+y] != color[(i+x+j+y+c)%2]) {
                    ++cnt;
                }
                
            }
        }
        rnt_cnt = min(rnt_cnt, cnt);
    }
    
    return rnt_cnt;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i <= N-8; ++i) {
        for (int j = 0; j <= M-8; ++j) {
            //cout << i << ", " << j << '\n';
            ans = min(fill_board(i, j), ans);
        }
    }


    cout << ans;

    return 0;
}