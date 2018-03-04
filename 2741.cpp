#include <iostream>
using namespace std;

int main()
{
  int N;
  cin >> N;
  for (int i = 1 ; i <= N ; i++)
      cout << i << "\n";
/* 처음에 두번이나 시간초과가 나왔는데,
그 이유가 endl; 을 써서 그렇다.
endl 대신에 \n을 써야 한다.
*/
  return 0;
}
