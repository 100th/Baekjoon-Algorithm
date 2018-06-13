#include <iostream>
#include <string>
using namespace std;

int main(){
	int arr[26];
//  배열 만든다
	string str;

	for (int i = 0; i < 26 ; i++){
		arr[i] = -1;
// 모든 배열을 -1로 초기화
	}

	cin >> str;
	for (int i = 0 ; i < str.size(); i++){
		for (int j = 0; j < 26; j++){
// 사실 for과 if의 반복이지만 어렵다
			if (str[i] == (int)'a' + j){
// 알파벳 'a'를 int로 받아서 아스키 코드로 받는다.
				if (arr[j] != -1){
					break;
				}
				else{
					arr[j] = i;
					break;
// 배열이 -1이라면 (즉, 그 알파벳이 하나도 없다면) i 할당
				}
			}
		}
	}
  for (int i = 0; i < sizeof(arr) / sizeof(int); i++){
// 이 부분이 제일 어렵다.
// i를 언제까지 for 안에서 돌려야하는지
// sizeof(int)....
		cout << arr[i] << " ";
	}
	return 0;
}
