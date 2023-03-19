#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, num;
vector<int> vec;



void solution1() {
    sort(vec.begin(), vec.end());
}

void solution2() {
    
}

int main() {
    /* INPUT */
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> num;
        vec.push_back(num);
    }

    /* SOLUTION */
    solution1();

    /* OUTPUT */
    for (int i = 0; i < N; ++i) {
        cout << vec[i] << '\n';
    }

    return 0;
}