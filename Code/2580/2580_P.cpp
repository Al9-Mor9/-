#include <iostream>
using namespace std;

int board[10][10];
bool RL[10][10];
bool UD[10][10];
bool square[10][10];
int cnt;

void sudoku(int cnt) {
	
	if (cnt == 81) {
		for (int i = 1; i < 10; i++) {
			for (int j = 1; j < 10; j++) {
				printf("%d ", board[i][j]);
			}
			printf("\n");
		}
		exit(0);
	}

	int i = cnt / 9 + 1;
	int j = cnt % 9 + 1;

	if (board[i][j]) sudoku(cnt + 1);

			if (!board[i][j]) {
				for (int k = 1; k < 10; k++) {
					if (!RL[i][k] && !UD[j][k] && !square[(i - 1) / 3 * 3 + (j - 1) / 3 + 1][k]) {
						board[i][j] = k;
						RL[i][k] = true;
						UD[j][k] = true;
						square[(i - 1) / 3 * 3 + (j - 1) / 3 + 1][k] = true;
						
						sudoku(cnt+1);
						
						board[i][j] = 0;	
						RL[i][k] = false;
						UD[j][k] = false;
						square[(i - 1) / 3 * 3 + (j - 1) / 3 + 1][k] = false;
					}
				}
			}
		
	
	
}

int main() {
	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			scanf(" %d", &board[i][j]);
			if (board[i][j]) {
				RL[i][board[i][j]] = true;
				UD[j][board[i][j]] = true;
				square[(i - 1) / 3 * 3 + (j - 1) / 3 + 1][board[i][j]] = true;
			}
		}
	}

	sudoku(0);	
}
