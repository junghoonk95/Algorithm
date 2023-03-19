#include<iostream>

using namespace std;
#define MAX 1000001
int N;
int tb[MAX];
int temp_tb[MAX];

void merge_sort(int s, int e) {
    int m = (s+e)/2;

    if(s >= e) return;

    merge_sort(s, m);
    merge_sort(m+1, e);

    int l = s, r = m+1;

    int cur = 0;
    while (cur < e - s + 1) {
        if(l <= m  && r <= e) {
            if(tb[l] > tb[r]) {
                temp_tb[cur++] = tb[r++];
            }
            else {
                temp_tb[cur++] = tb[l++];
            }
        }
        else {
            if(l <= m) {
                temp_tb[cur++] = tb[l++];
            }
            else if(r <= e) {
                temp_tb[cur++] = tb[r++];
            }
        }
    }
    copy(temp_tb, temp_tb + cur, tb + s);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; ++i) {
        cin >> tb[i];
    }
    merge_sort(0, N-1);

    for(int i = 0; i < N; ++i) {
        cout << tb[i] << "\n";
    }
}
