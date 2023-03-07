#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    // 오름차순 정렬
    sort(people.begin(), people.end());
    
    int idx = 0;
    int left = 0, right = people.size()-1;
    
    /*
    우선 (보트에 타지 않은&) 몸무게가 제일 많이 나가는 오른쪽 idx부터 태운다.
    인원 제한이 최대 2명이므로, 보트에 타지 않은 사람들중 가장 몸무게가 적게 나가는 사람을 골라 합을 비교한 후 태울지말지 결정.
    */
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            /*
            현재 left idx, right idx 의 사람 몸무게 합이 
            limit 을 넘지 않는다면, 둘 다 태운다 (left++, right--)
            */
            ++left;
        }
        --right;
        ++answer;
    }
    
    return answer;
}