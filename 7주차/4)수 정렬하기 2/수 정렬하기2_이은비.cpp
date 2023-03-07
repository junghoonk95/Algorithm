#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, num;
vector<int> vec, vec2;
int sort_list[1000001];

void solution1() { // sort()
    sort(vec.begin(), vec.end());
}

void merge_(int list[], int start, int mid, int end) {
    int left = start, right = mid+1;
    int idx = start;

    while (left <= mid && right <= end) {
        if (list[left] <= list[right]) {
            sort_list[idx++] = list[left++];
        }
        else {
            sort_list[idx++] = list[right++];
        }
    }

    while (left <= mid) {
        sort_list[idx++] = list[left++];
    }
    while (right <= end) {
        sort_list[idx++] = list[right++];
    }

    for (int i = start; i <= end; ++i)
        list[i] = sort_list[i];
}

void merge_sort(int list[], int start, int end) {
    if (start < end) {
        int mid = (start+end) / 2;
        merge_sort(list, start, mid);
        merge_sort(list, mid+1, end);
        merge_(list, start, mid, end);
    }
}


void quick_sort_TO(int a, int b) {
    if (a >= b) return ;

    int pivot = a, temp;
    int left = a+1, right = b;

    while (left <= right) {
        // pivot 보다 큰놈을 만나기 전까지 Left point 이동.
        while (vec[pivot] >= vec[left] && left <= b)
            ++left;

        // pivot 보다 작은놈을 만나기 전까지 right point 이동.
        while (vec[pivot] <= vec[right] && a < right)
            --right;

        if (left > right) {
            temp = vec[right];
            vec[right] = vec[pivot];
            vec[pivot] = temp;
        }
        else {
            temp = vec[left];
            vec[left] = vec[right];
            vec[right] = temp;
        }
    }

    quick_sort_TO(a, right-1);
    quick_sort_TO(right+1, b);
}


int main() {
    /* INPUT */
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;

    int list[N];
    for (int i = 0; i < N; ++i) {
        cin >> list[i];
        // vec.push_back(num);
        // vec2.push_back(num);
    }
    
    /* SOLUTION */
    merge_sort(list, 0, N-1);

    /* OUTPUT */
    for (int i = 0; i < N; ++i) {
        cout << list[i] << '\n';
    }

    return 0;
}