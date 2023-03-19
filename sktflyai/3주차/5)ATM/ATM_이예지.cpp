#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n; //사람 수
vector<int> time; //인출하는 데에 필요한 시간 

int main()
{
    int answer = 0;
    int t_sum = 0;
    int x;

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> x;
        time.push_back(x);
    }

    //오름차순 정렬
    sort(time.begin(), time.end());

    for(int i=0; i<n; i++){
        t_sum += time[i];
        answer += t_sum;
    }
    
    cout << answer;
    
    return 0;
}
