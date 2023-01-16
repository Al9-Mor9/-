#include <iostream>
#include <math.h>

int board[14];
int N;
int count = 0;

void queen(int num) {
	if (num == N) { count++; return; }
	bool newqueen;
	for (int i = 0; i < N; i++) {
		newqueen = true;
		for (int j = 0; j < num; j++) {
			if (i == board[j] || abs(j - num) == abs(i - board[j])) { newqueen = false; break; }
		}
		if (newqueen) {
			board[num] = i;
			queen(num + 1);
		}
	}

}

int main() {
	scanf("%d", &N);
	queen(0);
	printf("%d", count);
}
