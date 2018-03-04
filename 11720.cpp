#include <iostream>
using namespace std;

int main(void)
{
  int n;
  cin >> n;
  char ch; // 하나씩 받아야 하므로
  int sum = 0;
  for ( int i = 0 ; i < n ; i++ )
  {
    cin >> ch;
    sum += ( ch - '0' ); // int 타입으로 변환하여
  }
  cout << sum;
  return 0;
}
