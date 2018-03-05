#include <iostream>
using namespace std;
int main()
{
  long long n; // 64비트 정수
  cin >> n;
//계산
  int cnt = 1; //몇겹인지 = 최소 칸수
  long long range =1; //숫자의 범위
  long long tmp =1; //6의 배수를 더하기 위해

  while(1){
    if(range >= n){
      //숫자의 범위가 커지면 break;
      break;
    }
    tmp = 6 * (cnt++);
    range += tmp;
  }
//출력
  cout << cnt;
  return 0;
}
