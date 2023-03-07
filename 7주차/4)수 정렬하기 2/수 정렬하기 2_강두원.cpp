#include<iostream>

using namespace std;
#define MAX 1000001
int N;
int tb[MAX];
int temp_tb[MAX];

void merge_sort(int s, int e) {
    if(s >= e) return;

    // divide step //
    int m = (s+e)/2;
    merge_sort(s, m);
    merge_sort(m+1, e);
 
    // conquer & merge step //
    int l = s, r = m+1;
    for(int i = 0; i < e-s+1; ++i){
        // compare 2 arrays
        if(l <= m  && r <= e) {
            // add a smaller one to temp
            if(tb[l] > tb[r]) temp_tb[i] = tb[r++];
            else temp_tb[i] = tb[l++];
        }
        // append the rest array to temp
        else {
            if(r <= e) temp_tb[i] = tb[r++];
            else if(l <= m) temp_tb[i] = tb[l++];
        }
    }

    // apply temp to tb
    copy(temp_tb, temp_tb + e-s+1, tb + s);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; ++i) cin >> tb[i];

    merge_sort(0, N-1);

    for(int i = 0; i < N; ++i) cout << tb[i] << "\n";
}
