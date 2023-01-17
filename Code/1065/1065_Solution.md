# #1065 한수

## 풀이
#### 요약 
1000 이하의 자연수 N을 입력받고, N 이하의 자연수들 중 각 자리의 숫자들이 등차수열을 이루는 수(한수)가 몇 개 있는지 셉니다.   

#### 상세
100 미만의 모든 자연수 n은 **한수**입니다.
세 자리 수의 경우(100 ~ 999), (100의 자리 수 - 10의 자리 수) == (10의 자리 수 - 1의 자리 수)가 되면 **한수**입니다.

#### 코드 해제
<pre><code>
#include <iostream>
using namespace std;

bool isHansu(int n) {
	if (n < 100) return true; //iii) 100 미만의 모든 자연수는 한수입니다.
	if (n < 1000) return (n / 100 + n % 10 == n % 100 / 10 * 2); // iv) 각 자리 수가 등차수열을 이룬다면 한수입니다.
	return false; // v) 어느 것도 만족하지 않으면 한수가 아닙니다.
}

int main() {
	int N, ans = 0;
	scanf("%d", &N);  //i) N을 입력받고,
	for (int i = 1; i <= N; i++) {
		if (isHansu(i)) ans++; //ii) N 이하의 자연수들을 체크하면서 해당 수들이 한수라면 카운트해줍니다.
	}

	printf("%d", ans); // vi) 정답 출력

}
</code></pre>
