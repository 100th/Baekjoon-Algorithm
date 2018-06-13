#include <iostream>
using namespace std;

int count = 0;
int n;

int hansoo(int n)
{
  int n1 = (n % 100) % 10;
  int n2 = (n % 100) / 10;
  int n3 = n / 100;

  if ( n2 - n3 == n1 - n2 )
    count++;
  else if (n3 == 0)
    count++;
}

int main()
{
  cin >> n;
  for ( int i = 1 ; i <= n ; i++ )
    hansoo(i);

  cout << count << endl;

  return 0;
}
