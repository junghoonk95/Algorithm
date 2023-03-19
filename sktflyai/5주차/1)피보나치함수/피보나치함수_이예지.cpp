#include <iostream>
using namespace std;
long long arr[50] = {0,1,};
long long fibo(int N)
{
    if(N == 0 || N == 1)
        return arr[N];
    else if(arr[N] == 0)
        arr[N] = fibo(N-1) + fibo(N-2);
    return arr[N];
}
int main() {
    int T;
    cin >> T;
    int tmp;
    for(int i = 0; i < T; i++)
    {
        cin >> tmp;
        if(tmp == 0)
            cout << "1 0" << '\n';
        else
            cout << fibo(tmp-1) << ' ' << fibo(tmp) << '\n';
    }
}
