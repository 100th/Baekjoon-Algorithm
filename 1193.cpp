#include <iostream>
using namespace std;

int main(){
	int x, n, num;
	cin >> x;

	for ( int i = 1 ; i < x ; i++ ){
		int c = ( i * ( i + 1 ) ) / 2;
// 등차수열의 합 공식 {n*(n+1)}/2
		if ( c >= x ) // 해당하는 대각선에서 스톱
			break;
		n = i; // 몇 번째 대각선인지
		num = x - c;}
    // 수의 차를 통해서 대각선에서 몇 번째에 위치하는지

	n++; // n은 몇 번째 대각선인지
	int up,down; // 분자와 분모

  if ( n % 2 == 1 ){ // 홀수 번째 대각선
		up = n - num + 1; // 분자는 역순
		down = num; // 분모는 순서대로
	}else{ // 짝수 번째 대각선
    up = num; // 분자는 순서대로
		down = n - num + 1; // 분모는 역순
	}

	cout << up << '/' << down << '\n';
	return 0;
}
