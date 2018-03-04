#include <iostream>
using namespace std;

int main()
{
  int a, b, c;
  int arr[10] = {0};
// 10개짜리 배열을 만들어서 모두 0으로 초기화
  cin >> a >> b >> c;
  int result = a * b * c;

  int n[9] = {0};

  while(result != 0){
// 만약 곱이 0이 아니라면 계속 실행해라
      arr[result % 10] += 1;
      result /= 10;
// 계속 더하고, 계속 나누고. 그 과정을 기록한다.
  }

  for ( int k = 0 ; k <= 9 ; k++ )
    { cout << arr[k] << endl;}

  return 0;
}
