#include<stdio.h>
#include<vector>

#define INTMAX (1<<31) ^ -1

struct Point {
	int x, y;
};

int N, M;
int res = INTMAX;
int visit[50][50];
std::vector<std::vector<int>> table;

void dfs(Point start) {
	int x = start.x;
	int y = start.y;	
	if (visit[y][x] || x > M-8 || y > N-8) {
		return;
	}

	visit[y][x] = true;

	dfs({ x + 1, y });
	dfs({ x, y + 1 });

	int count = 0;
	int res_count;
	
	for (int k = 0; k <= 1; ++k) {
		for (int i = y; i < y + 8; ++i) {
			for (int j = x; j < x + 8; ++j) {
				int deter = ((i + j) & 1) ^ k;	//make checker board pattern
				if (deter == table[i][j]) {
					count++;
				}
			}
		}
		if (k == 0) {
			res_count = count;
			count = 0;
		}
		else {	//compare white first and black first
			res_count = res_count > count ? count : res_count;
		}
	}

	res = res > res_count ? res_count : res;
}

int main() {
	const Point start = { 0, 0 };
	char B[2] = { 'W', 'B' };

	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; ++i) {
		std::vector<int> vec;
		char temp[50];
		scanf("%s", &temp);

		for (int j = 0; j < M; ++j) {
			vec.push_back((temp[j] - 'B') & 1);
		}
		table.push_back(vec);
	}

	dfs(start);
	printf("%d\n", res);
}
