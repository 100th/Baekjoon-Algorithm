#include <iostream>
using namespace std;

int main()
{
  int n;
  n >= 1, n <= 100;
  cin >> n;
  for (int i = 0 ; i < n ; i++)
      {
      for (int j = 0 ; j < n ; j++)
// for의 첫 번째 값은 0으로 하는게 제일 편한 것 같다
        {
        if (j < n - i-1)
          cout << " " ;
// 공백 넣기. 여기가 중요하다.
        else
          cout << "*";
        }
      cout << "" <<endl;
    }
  return 0;
}
