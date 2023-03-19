#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, ans = 0;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;

    while (N > 0) {  // 무게 3, 5 가방밖에 없기 때문에 현재 남은 무게가 5로 나누어진다면 모두 무게 5 가방에 넣고, 아니라면 무게 3 가방에 넣어 0 이 될 때까지 반복함
        if (N%5 == 0) { // 무게 5의 가방에 모두 담을 수 있다면
            ans += N/5;
            N = 0;

            continue;
        }

        N -= 3; // 무게 3의 가방에 담는다
        ans += 1;
    }

    if (N < 0) cout << -1; // 무게가 0 으로 남지 않는다면 -> 가방에 적절히 담을 수 없음
    else cout << ans;

    return 0;
}