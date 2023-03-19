#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
char board[64][64];

void divide_paper(int x, int y, int n) {
    char check = board[x][y];
    for (int i = x; i < x+n; ++i) {
        for (int j = y; j < y+n; ++j) {
            if (check != board[i][j]) {
                cout << "(";
                divide_paper(x, y, n/2);
                divide_paper(x, y+n/2, n/2);
                divide_paper(x+n/2, y, n/2);
                divide_paper(x+n/2, y+n/2, n/2);
                cout << ")";
                
                return ;
            }
        }
    }
    cout << check;
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

    return 0;
}