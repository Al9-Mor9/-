#include <iostream>
using namespace std;

bool isHansu(int n) {
	if (n < 100) return true;
	if (n < 1000) return (n / 100 + n % 10 == n % 100 / 10 * 2);
	return false;
}

int main() {
	int N, ans = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		if (isHansu(i)) ans++;
	}

	printf("%d", ans);

}
