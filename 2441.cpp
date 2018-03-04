#include <iostream>
using namespace std;

int main()
{
  int n;
  n >= 1, n <= 100;
  cin >> n;
  for (int i = 0 ; i < n ; i++)
    {
      for(int k = 0 ; k < i ; k++)
        cout << " " ;

      for (int j = 0 ; j < n-i ; j++)
        {cout << "*" ;}

      cout << "" <<endl;
    }
  return 0;
}
