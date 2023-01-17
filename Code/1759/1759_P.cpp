#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int L, C, cnt;
char alphabets[15];
char vowel[5] = {'a', 'e', 'i', 'o', 'u'};
vector<char> possible;
map<vector<char>, int> ans;

bool isVowel(char c){
    for (int i = 0; i < 5; i++) {
        if (c == vowel[i]) return true;
    }
    return false;
}

bool isValid(vector<char> possible){
    int vowelCnt = 0;
    for (int i = 0; i < L; i++){
        if (isVowel(possible[i])) vowelCnt++;
    }
    if (vowelCnt && (L- vowelCnt) > 1) return true;
    return false;
}


int main(){
    scanf("%d%d", &L, &C);
    for (int i = 0; i < C; i++){
        cin >> alphabets[i];
    }
    for (int i = 0; i < (1 << C + 1) - 1; i++){
        cnt = 0;
        possible.clear();
        for (int j = 0; j < C; j++){
            if (possible.size() >= L) break;
            if (i & (1 << j)) possible.push_back(alphabets[j]);
        }
        if (possible.size() == L && isValid(possible) && !ans.count(possible)){
            sort(possible.begin(), possible.end());
            ans.insert({possible, 0});
        }
    }

    for (map<vector<char>, int>::iterator itr = ans.begin(); itr != ans.end(); itr++) {
        for (char c : itr->first) cout << c;
        cout << endl;
    }

}
