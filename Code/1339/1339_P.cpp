#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
    int N, d, ans = 0;
    char word[9];
    int alphabet[26] = {0, };
    scanf("%d", &N);

    for (int i = 0; i < N; i++){
        scanf("%s", word);
        d = 1;
        for (int j = strlen(word) - 1; j >= 0; j--){
            alphabet[word[j] - 'A'] += d;
            d *= 10;
        }
    }
    sort(alphabet, alphabet + 26, greater<>());
    for (int i = 0; i < 26; i++){
        if (alphabet[i] == 0) break;
        ans += (9 - i) * alphabet[i];
    }
    printf("%d", ans);

}
