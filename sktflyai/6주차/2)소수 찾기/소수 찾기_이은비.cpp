#include <string>
#include <vector>
#include <iostream>

// 주어진 숫자를 한 번만 사용할 수 있음.

// sol1 : 소수 배열을 먼저 만들고, 백트래킹으로 숫자 visit, 소수 확인

using namespace std;

vector<int> card;
vector<bool> used;
bool visited[10000000];
bool notPrime[10000000];
int numbers_leng, answer = 0;

void bt(int cnt, int num) { // 현재 자리수, 현재 만들어진 수, 사용된 카드(는 used로)...
    if (cnt > numbers_leng) return ;
    
    if (!visited[num]) {
        // cout << "visit " << num << '\t';
        visited[num] = true;
        
        // 소수인지 확인...
        if (!notPrime[num]) {
            // cout << "is prime";
            ++answer;
        }
        
        // cout << '\n';
        
    }
    
    for (int i = 0; i < numbers_leng; ++i) {
        if (!used[i]) {
            used[i] = true;
            // cout << "---";
            // cout << num << ' ' << card[i] << '\n';
            bt(cnt+1, num*10 + card[i]);
        
            used[i] = false;
        }
    }
}



int solution(string numbers) {
    // numbers
    numbers_leng = numbers.length();
    // input
    for (int i = 0; i < numbers_leng; ++i) {
        card.push_back(numbers[i]-'0');
        cout << card[i] << ' ';
        used.push_back(false);
    }
    // cout << '\n';
    
    
    // 에.체 = 소수 만들기
    notPrime[0] = true;
    notPrime[1] = true;
    for (int i = 2; i*i < 10000000; ++i) {
        if (!notPrime[i]) {
            for (int j = i*2; j < 10000000; j+=i) {
                notPrime[j] = true;
            }
        }
    }

    
    bt(0, 0);
   
    
    
    return answer;
}