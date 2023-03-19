#include <vector>
// 추가
#include <iostream>
#include <algorithm> 

using namespace std;

int solution(vector<int> people, int limit) {
    /*
    int answer = people.size();
    sort(people.begin(), people.end());
    for(int i = 0; i<people.size()/2; i=i+2){
        if(people[i] + people[i+1] <= limit)
            answer -= 1;
        else
            break;
    }*/
    //처음에 가벼운 사람만 먼저 태우기로 생각
    //limit에 딱 맞는 경우만 고려 => 남으면 비효율
    //제일 가벼운 사람 + 제일 무거운 사람 으로 고려
  
    int answer = 0;
    int front = 0; // 제일 가벼운 사람 index
    int back = people.size() - 1; // 제일 무거운 사람 index
    //입력값 오름차순 정렬
    sort(people.begin(), people.end());
    while(front <= back){
        if(people[front]+people[back]<=limit){//두명 태우기 가능하면
            front++;
            back--;
            // 두명 태우기
        }else
            back--; // 무거운 애만 태우기
        answer++;
    }
    return answer;
}
